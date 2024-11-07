"""
pyscreenshot is a module that allows you to take screenshots
It is a pure Python wrapper (a thin layer over existing backends)

Performance and interactivity are not important for this library

Use pip install pyscreenshot
"""



#Capturing full screenshot
import pyscreenshot

#to capture the screen
image = pyscreenshot.grab()

#display the captured screenshot
image.show()

#save the screenshot
image.save('py_screenshot.png')



