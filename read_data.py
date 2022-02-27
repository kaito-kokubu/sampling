import signal
import time
from unittest import result
from Subfact_ina219 import INA219
import ina219_example
import csv
import datetime
#import led

first_exec_time = 1 #1回目の実行までの時間 (s)
interval = 1 #2回目以降の実行間隔 (s)
read_data_time = 120 #計測時間 (s)

#led.led_start(read_data_time)

result_data = []

def scheduler(arg1, arg2):
    result = ina219_example.main()
    result_data.append(result)

#ina = INA219()
#print(ina)

signal.signal(signal.SIGALRM, scheduler)
signal.setitimer(signal.ITIMER_REAL, first_exec_time, interval)

try:
    while True:
        time.sleep(interval)
except KeyboardInterrupt:
    print("Keyboard Interrupted!")
    now = datetime.datetime.now()
    filename = "~/Desktop/sampling/output/log_" + now.strftime("%Y%m%d_%H%M%S") + ".csv"
    with open(filename) as f:
        writer = csv.writer(f)
        writer.writerows(result_data)
    print("Data saved!")
