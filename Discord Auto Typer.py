#Imports
import pyautogui
import time
import random
import keyboard

#Title Image and Credits
print("_____________________________________________________________________________________")
print("                     _______  _______    _______          _______   _______  _______")
print("    /\     |       |    |    |       |      |    \     / |       | |        |       | v1.5")
print("   /  \    |       |    |    |       |      |     \   /  |       | |        |       |")
print("  /----\   |       |    |    |       |      |      \ /   |_______| |_______ |_______|")
print(" /      \  |       |    |    |       |      |       |    |         |        |     \ ")
print("/        \ |_______|    |    |_______|      |       |    |         |_______ |      \ ")
print("_____________________________________________________________________________________")
print("                                   by IdleEndeavor")

#Text to be automatically run
text_1 = input("Text 1: ")
text_2 = input("Text 2: ")
text_3 = input("Text 3: ")
text_4 = input("Text 4: ")
text_5 = input("Text 5: ")

print("--> Hold Right Shift Key for 5 Seconds to Stop Program <--")

#Auto Typer
me = True
while keyboard.is_pressed("shift") == False:
    pyautogui.sleep(5)
    texts = {
        "1": text_1,
        "2": text_2,
        "3": text_3,
        "4": text_4,
        "5": text_5
    }
    number = random.randint(1,5)
    texter = texts.get(str(number))
    pyautogui.typewrite(texter)
    pyautogui.press("enter")
    print(texter)