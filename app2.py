from pynput import mouse

locations = []  # Store the four locations

def on_click(x, y, button, pressed):
    """Captures four (x, y) positions on mouse clicks."""
    if pressed:
        locations.append((x, y))
        print(f"Captured location {len(locations)}: {x}, {y}")

        if len(locations) == 4:
            print("All four locations captured:", locations)
            return False  # Stop listener after four clicks

# Start the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    print("Click four times to capture the locations...")
    listener.join()

# Print final locations
print("Final captured locations:", locations)
