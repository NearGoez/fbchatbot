from PIL import ImageGrab
import pyautogui
import keyboard
import win32api, win32con
import time

with open("userdata.txt", "r") as f:
        udata = f.read() 
        udata = udata.split("\n")
        for i,x in enumerate(udata):
            udata[i] = x.split("#")
for x in udata:
   print(x[0])

def columna():
    try:
        img = pyautogui.locateOnScreen("columnablanca.png", region=(538, 228, 7, 360 ))
        if img != None:
            return 1
    except: 
        return 0 

def imagen2(foto):
    try:
        img = pyautogui.locateOnScreen(foto, region=(76, y-21, 50, 50), confidence=(0.9))
        if img != None:
            return 1
    except: 
        return 0
def click(x, y, t):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pantalla = ImageGrab.grab()
while True:
    for y in range(1, 825):
        color = pantalla.getpixel((378, y ))
        if color[1]==153:
            click(280, y, 0.1)
            time.sleep(0.8)
            pantalla = ImageGrab.grab()
            if columna()==1:
                for x in udata:
                    if imagen2(x[0])==1:    
                        time.sleep(1)
                        pyautogui.typewrite(x[1])
                else:   
                    win32api.SetCursorPos((352, 152)) 
                    time.sleep(0.1)
                    click(352, y, 0.1)
                    click(352, y+60 , 0.1) 
                    y = y+8
                    time.sleep(1)
                    pantalla = ImageGrab.grab()      
                
    click(412, 1024, 1)
    time.sleep(1.5)
    pantalla = ImageGrab.grab()

    
