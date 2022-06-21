import pyautogui as pt
import time
count=1
while count<=100:
    pt.moveTo(10,10)
    pt.click()
    time.sleep(1)
    pt.type("Hello World")
    time.sleep(1)
    pt.press("enter")
    