import mouse 
from PIL import ImageGrab 
import pyautogui
import time 


##mouse.click("left") acciona click izquierdo

while True:
    cursor = pyautogui.position()
    screen = ImageGrab.grab() 
    print(cursor, screen.getpixel((cursor)))
    time.sleep(0.05)

