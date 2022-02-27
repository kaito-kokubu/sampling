import signal
import time
from unittest import result
from Subfact_ina219 import INA219
import ina219_example
import csv
import datetime
import os
import RPi.GPIO as GPIO


def scheduler(arg1, arg2):
    if i == 50:
        GPIO.output(25, GPIO.HIGH)
        led_on = True
    result = ina219_example.main()
    if led_on:
        result.append('on')
    else:
        result.append('off')
    result_data.append(result)
    i += 1

def main():
    signal.signal(signal.SIGALRM, scheduler)
    signal.setitimer(signal.ITIMER_REAL, first_exec_time, interval)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard Interrupted!")
        print(os.getcwd())
        now = datetime.datetime.now()
        filename = "/home/pi/Desktop/sampling/output/log_" + now.strftime("%Y%m%d_%H%M%S") + ".csv"
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result_data)
        print("Data saved!")
        GPIO.output(25, GPIO.LOW)

result_data = []
i = 0
led_on = False

first_exec_time = 5 #1回目の実行までの時間 (s)
interval = 0.1 #2回目以降の実行間隔 (s)
#read_data_time = 120 #計測時間 (s)

#led.led_start(read_data_time)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

main()
