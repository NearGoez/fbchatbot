#print("q para encender/apagar \nw para agregar una publicación \ne para editar un mensaje")
import pyautogui

with open("userdata.txt", "r") as f:
        udata = f.read() 
        udata = udata.split("\n")
        del udata[-1]
        for i,x in enumerate(udata):
            udata[i] = x.split("#")

with open("userdata.txt", "a") as f:
    for x in range(int(input())):

        added = f"{input("ingrese el nombre de la imagen ")}#{input("ingrese el mensaje que desee ")} \n"
        f.write(added)
for x in udata: 
    if pyautogui.locateOnScreen(x[0]) != None:
        print(x[1])
