from RPi import GPIO as gpio
from gpiozero import CPUTemperature
from threading import Event

import logging, os
from pathlib import Path


logger = logging.getLogger('test')
FORMAT = logging.Formatter('%(levelname)s: %(asctime)s, %(message)s')
path = Path('fancontroller_log', 'log.txt')
filehandler = logging.FileHandler(path, mode='a+', encoding='utf-8', delay=False)
filehandler.setFormatter(FORMAT)
logger.addHandler(filehandler)
logger.setLevel(logging.DEBUG)
os.chmod(path, 0o777)

def insertdebug(message):
    logger.debug(message)

def run(newRound):
    pwm = None
    temp = None
    try:
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.OUT)
        pwm = gpio.PWM(18, 300)
        pwm.start(100)
        while not newRound.wait(20):
            temp = CPUTemperature().temperature
            #print(temp)
            if temp > 75:
                pwm.ChangeDutyCycle(100)
            elif temp > 65:
                pwm.ChangeDutyCycle(80)
            elif temp > 55:
                pwm.ChangeDutyCycle(70)
#            elif temp > 50:
#                pwm.ChangeDutyCycle(50)
#            elif temp > 45:
#                pwm.ChangeDutyCycle(30)
            else:
                pwm12.ChangeDutyCycle(0)
    except Exception as e:
        newRound.set()
        insertdebug(e)
        pwm.stop()
        gpio.cleanup()

if __name__ == '__main__':
    newRound = Event()
    run(newRound)
