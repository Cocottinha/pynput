# from PIL import Image, ImageGrab
# import getpixelcolor
# vrau = getpixelcolor.pixel(958,882)

# px = ImageGrab.grab().load()
# for y in range(0, 100, 10):
#     for x in range(0, 100, 10):
#         color = px[x, y]
        
# print(f"Captured location: {vrau}")

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import time
import serial
import pyautogui

mouse = MouseController()
keyboard = KeyboardController()

ser = serial.Serial('COM3', 115200, timeout=1)

button1_location = (65, 412)  
button2_location = (69, 500)  
button3_location = (246, 359)  
button4_location = (614, 473)
counter = 0

def click_button(location):
    """Moves the mouse to the given location and clicks."""
    mouse.position = location
    time.sleep(0.2)  
    mouse.click(Button.left, 1)
    print("clicou", mouse.position)

def update_counter():
    """Types the current counter value."""
    keyboard.type(str(counter))

def verificar_pixel_verde(x, y):
    """Check if the board is already ready to run another measure"""
    # Captura a cor do pixel na posição (x, y)
    pixel = pyautogui.pixel(x, y)

    # Cor verde "puro" seria (0, 255, 0), mas podemos aceitar um intervalo
    r, g, b = pixel
    if g == 128 and r == 0 and b == 0:
        return True
    return False

def monitorar_pixel(x, y):
    while True:
        if verificar_pixel_verde(x, y):
            print(f"Pixel em ({x}, {y}) está verde!")
        else:
            print(f"Pixel em ({x}, {y}) NÃO está verde.")
        time.sleep(1)  # espera 1 segundo

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

send_gcode("G91")  # Set to relative positioning mode

for i in range(360):  # Loop 180 times
    print(f"Iteration {i}/360")
    
    click_button(button1_location)  # Click to acquire image
    monitorar_pixel(271, 1002) #preciso descobrir o pixel ainda
    time.sleep(1)
    #time.sleep(12)  # Foi utilizado 15s nos testes, mas 12 aparenta ser o necessário
    click_button(button2_location)  # Click to save image
    time.sleep(0.5)
    click_button(button3_location)  # Click to write the filename
    update_counter()  # Type counter value
    time.sleep(1)

    counter += 1  # Increment counter
    click_button(button4_location)  # Click to save
    time.sleep(1)  # Short delay before the next iteration
    
    # Move the motor 1 step at the end of the iteration
    try:
         # is X5 because the motor is attached to a "goniometro"
        send_gcode("G1 X5 F100")
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Movement interrupted")

ser.close()  # Close the serial connection after all iterations are done

print("Process completed!")
