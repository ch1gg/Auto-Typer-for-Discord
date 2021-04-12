#Imports
import pyautogui
import time
import random
import keyboard
from tkinter import *

root = Tk()
root.title("Auto Typer")
root.geometry("875x515")
root.configure(bg = "white")

text = Text(root, height=1, width=875, font = "BOLD")
text.pack()
text.insert("1.0", " _____________________________________________________________________________________")
text['state'] = "disabled"

text = Text(root, height=1, width=875)
text.pack()
text.insert("1.0", "                      _______  _______    _______          _______   _______  _______")
text['state'] = "disabled"

text = Text(root, height=1, width=875)
text.pack()
text.insert("1.0", "     /\     |       |    |    |       |      |    \     / |       | |        |       |")
text['state'] = "disabled"

text = Text(root, height=1, width=875)
text.pack()
text.insert("1.0", "    /  \    |       |    |    |       |      |     \   /  |       | |        |       |")
text['state'] = "disabled"

text = Text(root, height=1, width=875)
text.pack()
text.insert("1.0", "   /----\   |       |    |    |       |      |      \ /   |_______| |_______ |_______|")
text['state'] = "disabled"

text = Text(root, height=1, width=875)
text.pack()
text.insert("1.0", "  /      \  |       |    |    |       |      |       |    |         |        |     \ ")
text['state'] = "disabled"

text = Text(root, height=1, width=875)
text.pack()
text.insert("1.0", " /        \ |_______|    |    |_______|      |       |    |         |_______ |      \ ")
text['state'] = "disabled"

text = Text(root, height=1, width=875, font = "BOLD")
text.pack()
text.insert("1.0", " _____________________________________________________________________________________")
text['state'] = "disabled"

text = Text(root, height=1, width=875)
text.pack()
text.insert("1.0", "                                    by IdleEndeavor")
text['state'] = "disabled"

entry1 = Entry(root, width = 30, borderwidth = 5, relief = RIDGE)
entry1.pack(pady = 5)

entry2 = Entry(root, width = 30, borderwidth = 5, relief = RIDGE)
entry2.pack(pady = 5)

entry3 = Entry(root, width = 30, borderwidth = 5, relief = RIDGE)
entry3.pack(pady = 5)

entry4 = Entry(root, width = 30, borderwidth = 5, relief = RIDGE)
entry4.pack(pady = 5)

entry5 = Entry(root, width = 30, borderwidth = 5, relief = RIDGE)
entry5.pack(pady = 5)

def button_command():
    #Text to be automatically run
    text_1 = entry1.get()
    text_2 = entry2.get()
    text_3 = entry3.get()
    text_4 = entry4.get()
    text_5 = entry5.get()

    #Script to automatically go through and type 
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
        pyautogui.typewrite(str(texter))
        pyautogui.press("enter")
        print(texter)

Button(root, text = "Start", command = button_command, padx = 20, relief = RAISED).pack(pady = 10)

text = Text(root, height=1, width=875, relief = RAISED, font = "BOLD")
text.pack()
text.insert("1.0", "                             --> Hold Right Shift Key for 5 Seconds to Stop Program <--")
text['state'] = "disabled"

me = True
while me == True:
    text.update()

root.mainloop()