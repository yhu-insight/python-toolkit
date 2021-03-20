# -*- coding: utf-8 -*-

# Python Mouse Cursor
# Author - yucheng.hu@insight.com

import time

import pyautogui

while True:
    # Moving Mouse Cursor
    pyautogui.moveTo(x=300, y=300, duration=0.1)
    time.sleep(3)

    # Moving Mouse Cursor then click left side of mouse
    pyautogui.click(x=700, y=300, duration=0.1)
    time.sleep(3)

    # Moving Mouse Cursor then double click left side of mouse
    pyautogui.doubleClick(x=600, y=300, duration=0.1)
    time.sleep(3)

    # Moving Mouse Cursor then click right side of mouse
    pyautogui.rightClick(x=700, y=300, duration=0.1)
    time.sleep(3)

    pyautogui.click(x=100, y=200)
    time.sleep(10)

    pyautogui.click(x=200, y=400)
    time.sleep(10)

    # In windows open Paint then run code below
    distance = 200
    while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)  # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)  # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up
    time.sleep(10)



