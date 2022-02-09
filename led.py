import RPi.GPIO as GPIO
from time import sleep

def led_start(how_long_LED):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)

    i = 0
    while True:
        GPIO.output(25, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(25, GPIO.LOW)
        sleep(0.5)
        i += 1
        if i >= how_long_LED:
            break
    GPIO.output(25, GPIO.LOW)