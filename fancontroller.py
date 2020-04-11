from RPi import GPIO as gpio
from gpiozero import CPUTemperature
from threading import Event

import logging, os
from pathlib import Path


logger = logging.getLogger('fan.controller')
FORMAT = logging.Formatter('%(levelname)s: %(asctime)s, %(message)s')

if not os.path.exists('fancontroller_log'):
    os.makedirs('fancontroller_log')
path = Path('fancontroller_log', 'log.txt')
filehandler = logging.FileHandler(path, mode='a+', encoding='utf-8', delay=False)
filehandler.setFormatter(FORMAT)
logger.addHandler(filehandler)
logger.setLevel(logging.DEBUG)
os.chmod(path, 0o777)

def insertdebug(message):
    logger.debug(message)


temp = None
pwm12 = None
# input 11 for incidental use, if want read fan speed (not implemented yet)
# input11 = None

def run(pwm12, newRound):
    '''
    Run controlling until an error occured
    :param pwm12:
    :param newRound:
    :return:
    '''
    try:
        gpio.setmode(gpio.BCM)
        gpio.setup(12, gpio.OUT)# PWM cable connected to GPIO12
        pwm12 = gpio.PWM(12, 300)# 300 Hz because I have tested with a KDB0605HB laptop cooler
        pwm12.start(100)
        while not newRound.wait(10):
            temp = CPUTemperature().temperature
            # print(temp)
            if temp > 75:
                pwm12.ChangeDutyCycle(100)
                # print('actual dutycycle: ', 100)
            elif temp > 65:
                pwm12.ChangeDutyCycle(80)
                # print('actual dutycycle: ', 80)
            elif temp > 55:
                pwm12.ChangeDutyCycle(60)
                # print('actual dutycycle: ', 60)
            elif temp > 45:
                pwm12.ChangeDutyCycle(40)
                # print('actual dutycycle: ', 40)
            elif temp > 40:
                pwm12.ChangeDutyCycle(20)
                # print('actual dutycycle: ', 100)
            else:
                # the KDB0605HB stopped under 15% at 300Hz, under 36% at 200Hz and under 50% at 100 Hz
                pwm12.ChangeDutyCycle(1)
                print('fan stopped')
    except Exception as e:
        newRound.set()
        insertdebug(e)
        pwm12.stop()
        gpio.cleanup()


newRound = Event()
run(pwm12, newRound)
