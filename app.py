from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import time

mouse = MouseController()
keyboard = KeyboardController()

# Define button locations
button1_location = (116, 1056)  # First button coordinates
button2_location = (364, 347)  # Second button coordinates
counter = 1  # Start counter

def click_button(location):
    """Moves the mouse to the given location and clicks."""
    mouse.position = location
    time.sleep(0.2)  # Delay for stability
    mouse.click(Button.left, 1)

def update_counter():
    """Types the current counter value."""
    keyboard.type(str(counter))

# Repeat the process 180 times
for i in range(180):
    print(f"Iteration {i+1}/180")
    click_button(button1_location)  # Click first button
    time.sleep(10)  # Wait 10 seconds
    click_button(button2_location)  # Click second button
    update_counter()  # Type counter value
    counter += 1  # Increment counter
    time.sleep(1)  # Short delay before the next iteration

print("Process completed!")


# from pynput import mouse
# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))

# # Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()
#------------------------------------------------------------
# mouse = Controller()

# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))

# # Set pointer position
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(
#     mouse.position))

# # Move pointer relative to current position
# mouse.move(5, -5)

# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# # Double click; this is different from pressing and releasing
# # twice on macOS
# mouse.click(Button.left, 2)

# # Scroll two steps down
# mouse.scroll(0, 2)
#-------------------------------------------------------------
# def on_press(key):
#     try:
#         print(f'Key {key.char} pressed')
#     except AttributeError:
#         print(f'Special key {key} pressed')
    
# def on_release(key):
#     if key == keyboard.Key.esc:
#         print('Exiting program')
#         return False

# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
#