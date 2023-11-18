"""
Created by: Sophie
Created on: Nov 2023
This module is a Micro:bit MicroPython program makes servo rotate 0 and 180 degrees
"""

from microbit import *
import math


# in order to use servo
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_digital(0)  # turn the pin off

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

# setup
display.clear()
display.show(Image.HEART)
sleep(1000)

while True:
    # button a is pressed
    if button_a.is_pressed():
        # change servo to 0 degrees
        for angle in range(0, 40, 2):
            Servo(pin0).write_angle(0)

        # shows degree survo is turning to
        display.scroll("0")

        display.show(Image.HEART)
        display.clear()
        display.show(Image.HEART_SMALL)

    # button b is pressed
    if button_b.is_pressed():
        # change servo to 180 degrees
        for angle in range(0, 40, 2):
            Servo(pin0).write_angle(180)

        # shows degree survo is turning to
        display.scroll("180")

        display.show(Image.HEART)
        display.clear()
        display.show(Image.HEART_SMALL)
