"""
Created by: Sophie
Created on: Nov 2023
This module is a Micro:bit MicroPython program makes servo rotate 0 and 180 degrees
"""

from microbit import *

# from servo.py import the Servo class
from servo import Servo


# setup
display.clear()
display.show(Image.HEART)
sleep(1000)

while True:
    if button_a.is_pressed():
        # change servo to 0 degrees
        Servo(pin0).write_angle(0)
        display.scroll("0")

        display.show(Image.HEART)
        display.clear()
        display.show(Image.HEART_SMALL)

    if button_b.is_pressed():
        # change servo to 0 degrees
        Servo(pin0).write_angle(180)
        display.scroll("180")

        display.show(Image.HEART)
        display.clear()
        display.show(Image.HEART_SMALL)
