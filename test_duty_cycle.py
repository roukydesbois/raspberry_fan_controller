# for testing only
# run from terminal and listen when cooler stops
# then adjust second argument of gpio.PWM() function
# if cooler stops when countdown is under 10, you can modify same value in fancontroller.py on tested value

from RPi import GPIO as gpio
from gpiozero import CPUTemperature
from time import sleep
from threading import Thread, Event

temp = None
pwm12 = None
input11 = None

try:
    gpio.setmode(gpio.BCM)
    gpio.setup(18, gpio.OUT)
    # adjust second argument of gpio.PWM() function if necessary
    pwm12 = gpio.PWM(18, 300)
    pwm12.start(100)
    for i in range(100, -1, -1):
        pwm12.ChangeDutyCycle(i)
        print(i)
        sleep(1)
    pwm12.ChangeDutyCycle(0)

except Exception as e:
    print(e)

pwm12.stop()
gpio.cleanup()
