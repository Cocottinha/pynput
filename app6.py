from PIL import Image, ImageGrab
import getpixelcolor
import time


time.sleep(5)
vrau = getpixelcolor.pixel(271, 1002)
# px = ImageGrab.grab().load()
# for y in range(0, 100, 10):
#     for x in range(0, 100, 10):
#         color = px[x, y]
        
print(f"Captured location: {vrau}")