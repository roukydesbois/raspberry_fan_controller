# Raspberry fan controller
Simple python script for control speed of a pwm cooling fan.

Tested with a KDB0605HB laptop cooler on a Raspbery Pi 4, Ubuntu server 19.10.

### Dependencies:

- python3 (installed and made default by update-alternatives)
- package RPi.GPIO
- package gpiozero

### How to use:
I assume you connected to Pi via SSH before (Ubuntu server has it and started it by default). [ReferenceLink](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu)
  1. Download packages with pip
     `$ pip install RPi.GPIO gpiozero`
  2. Copy fancontroller.py to user directory (in my case /home/ubuntu)
  3. Create cron job:
     - open crontab:
       `$ sudo crontab -e`
     - insert a new line and paste
       `@reboot /path/to/python3 /path/to/fancontroller.py`
       + e.g.: "@reboot /usr/bin/python3 /home/ubuntu/fancontroller.py" in my case
     - save and exit
  4. Reboot Pi and script should work after system startup

### Note:
I am using Raspberry Pi 4 with KDB0605HB blower fan - whitch is a part of an Asus laptop - as my own DIY project.
300Hz was quite appropriate as PWM output frequency for this cooler, but if you have another type ([for example this one](https://www.amazon.com/Noctua-NF-A4x20-5V-PWM-Premium-Quality/dp/B071FNHVXN)), this can be different.

### References:
[How to use soft PWM in RPi.GPIO 0.5.2a pt 2 – led dimming and motor speed control](https://raspi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control)
[Raspberry Pi: PWM in GPIO (Python)](https://www.radishlogic.com/raspberry-pi/raspberry-pi-pwm-gpio/)
[RPi.GPIO basics 4 – Setting up RPi.GPIO, numbering systems and inputs](https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs)
[class gpiozero.CPUTemperature](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature)

##### P. S.
This is my first uploaded project, so execuse me if experience any deficiency on my commit...
