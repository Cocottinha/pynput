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

ser = serial.Serial('COM12', 115200, timeout=1)

button1_location = (45, 513)  
button2_location = (55, 625)  
button3_location = (63, 621)  
button4_location = (731, 575)
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

def esperar_pixel_verde(x, y):
    """Espera até que o pixel em (x,y) fique verde"""
    while True:
        r, g, b = pyautogui.pixel(x, y)
        if g == 128 and r == 0 and b == 0:  # Verde dentro de um intervalo
            print(f"Pixel em ({x}, {y}) ficou VERDE! Continuando...")
            return True
        else:
            print(f"Pixel em ({x}, {y}) ainda não está verde ({r}, {g}, {b})...")
            time.sleep(1)  # espera 1 segundo antes de checar de novo


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

  # Set to relative positioning mode
time.sleep(5)
for i in range(360):  # Loop 180 times
    print(f"Iteration {i}/360")
    
    
    click_button(button1_location)  # Click to acquire image
    time.sleep(2)
    esperar_pixel_verde(271, 1002) #preciso descobrir o pixel ainda
    # #time.sleep(12)  # Foi utilizado 15s nos testes, mas 12 aparenta ser o necessário
    time.sleep(1)
    click_button(button2_location)  # Click to save image
    time.sleep(0.5)
    click_button(button3_location)  # Click to write the filename
    update_counter()  # Type counter value
    time.sleep(1)

    counter += 1  # Increment counter
    click_button(button4_location)  # Click to save
    time.sleep(1)  # Short delay before the next iteration
    try:
        send_gcode("G91")
        send_gcode("G1 X5 F100")
        time.sleep(2)
    except KeyboardInterrupt:
        print("Movement interrupted")
    # Move the motor 1 step at the end of the iteration
    

ser.close()  # Close the serial connection after all iterations are done

print("Process completed!")
