#!/usr/bin/env python 3
# _*_ coding: utf-8 -*-

'''pip intall pyautogui '''

import pyautogui

speed = int(input('How fast should it scroll'))
sleepTime = int(input('How long to the next scroll'))

pyautogui.time.sleep(3)

while 0 < 10:
    pyautogui.scroll(speed)

    pyautogui.time.sleep(sleepTime) 