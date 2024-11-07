"""
We can also capture part of the screen by providing pixel positions to the grab() function
"""

#program for partial screenshot
import pyscreenshot as ImageGrab

#im = pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image = ImageGrab.grab(bbox=(10, 10, 500, 500))

#to view the screenshot
image.show()

#to save the screenshot
image.save('partial_screen.png')