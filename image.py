import pyautogui
import win32api, win32con
import time
def click(x, y, t):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


if pyautogui.locateOnScreen("columnablanca.png", region=(538, 228, 7, 360 )) != None:
    print("se encontró ")
else:   
    win32api.SetCursorPos((352, 152))
    time.sleep(0.1)
    click(352, 152, 0.1)
    click(352, 205, 0.1)   

