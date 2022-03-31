from PIL import ImageGrab
from PIL import ImageOps
import pyautogui, keyboard
import time
from numpy import *


drum_btn = 326, 432
drum_hit_loc = 541, 439


def drum_red():
    pyautogui.press('d')

#baloon = 83


def check_color(img):
    global current_color
    for x in range(0, img.width, 1):
        for y in range(0, img.height, 1):
            r, g, b = img.getpixel((x, y))
            # print(r)
            if(r==243 and g==71 and b==40):
                current_color = "red"
                return True
            if(r==248 and g==119 and b==0):
                current_color = "balloon"
                return True
            if(r==101 and g==189 and b==187):
                current_color = "blue"
                return True
            if(r==243 and g==181 and b==0):
                current_color = "gold"
                return True
    current_color = '============='

            # if b == 195 and r == 255 and g == 219:
            #     return drum_hit()d

def img_grab():
    # box = (520, 420, 40, 30)
    # box = (530, 430, 20, 15)
    # box = (550, 420, 15, 25)

    box = (550, 420, 15, 10) # good
    # box = (550, 400, 25, 10) # small
    # box = (560, 400, 20, 10)
    img = pyautogui.screenshot(region=box)
    check_color(img)
    global num
    if(num <=4):
        img.save(f'{num}.png')
        num+=1


global current_color, num
current_color = ""
num = 0


time.sleep(3)


while 1:
    color_before = current_color
    img_grab()
    # time.sleep(0.05)
    if current_color == 'gold':
        pyautogui.press('f')
        # time.sleep(0.01)
        pyautogui.press('d')
        print(current_color)

    if current_color == "balloon":
        pyautogui.press('f')
        #time.sleep(0.01)
        print(current_color)

    if color_before != current_color:
        if current_color == 'red':
            pyautogui.press('f')
        if current_color == 'blue':
            pyautogui.press('d')
        print(current_color)

