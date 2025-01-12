#source : https://www.youtube.com/watch?v=Di6ilGd0Y2M

#importing the pyautoGUi 
import pyautogui as pag
import time as tm

#control the mouse movements, clicks, drags, scroll

#get resolution of the primary screen 
print(pag.size())

#get position of the cursor 
x,y = pag.position()

#check if the cursor is on the screen 
print(pag.onScreen(x,y))

#move the mouse cursor 
#inputs (x,y,time in seconds)
pag.moveTo(1000,20,1)

#move relative will add on to the currentposition of the cursor and move the cursor
pag.moveRel(100,200,1)

#mouse click note:by default the click will be left click
#input parameter (x, y, click= , duation= inseconds, button= "left or right")
pag.click(1013, 1050, clicks=1,duration=1)
#pag.doubleClick()
# pag.rightClick()
# pag.leftClick()
# pag.tripleClick()

#scrolls up and down
# pag.scroll(500)
# pag.mouseDown()
# pag.mouseUp()

#keyboard operation

#only data can be written without any operation such as copy, paste and function keys etc;
pag.click()
pag.hotkey("ctrl","f")

pag.write("Hello !")

