from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import time
import serial

# Initialize the mouse, keyboard, and serial connection
mouse = MouseController()
keyboard = KeyboardController()

# Serial configuration
ser = serial.Serial('COM12', 115200, timeout=1)

time.sleep(2)  # Wait for the serial connection to initialize

# Define button locations
button1_location = (65, 412)  # First button coordinates
button2_location = (69, 500)  # Second button coordinates
button3_location = (246, 359)  # Third button coordinates
button4_location = (614, 473)  # Fourth button coordinates
counter = 1  # Start counter

def click_button(location):
    """Moves the mouse to the given location and clicks."""
    mouse.position = location
    time.sleep(0.2)  # Delay for stability
    mouse.click(Button.left, 1)
    print("clicou", mouse.position)

def update_counter():
    """Types the current counter value."""
    keyboard.type(str(counter))

def send_gcode(command):
    """ Sends a G-code command and prints the response """
    if ser.is_open:  # Check if the serial port is open
        ser.write((command + '\n').encode())  
        time.sleep(0.5)  # Wait for response
        response = ser.readlines()  # Read the response lines
        for line in response:
            print(line.decode().strip())  # Print the response to the terminal
    else:
        print("Error: Serial port is not open")

# Repeat the process 180 times
send_gcode("G91")  # Set to relative positioning mode

for i in range(180):  # Loop 180 times
    print(f"Iteration {i+1}/180")
    
    click_button(button1_location)  # Click to acquire image
    time.sleep(12)  # Foi utilizado 15s nos testes, mas 12 aparenta ser o necessário
    click_button(button2_location)  # Click to save image
    time.sleep(1)
    click_button(button3_location)  # Click to write the filename
    update_counter()  # Type counter value
    time.sleep(1)

    counter += 1  # Increment counter
    click_button(button4_location)  # Click to save
    time.sleep(1)  # Short delay before the next iteration
    
    # Move the motor 1 step at the end of the iteration
    try:
         # Absolute positioning mode
        send_gcode("G1 X1 F100")  # Move motor 1 step in X direction
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Movement interrupted")

# Close the serial connection after the loop
ser.close()  # Close the serial connection after all iterations are done

print("Process completed!")
