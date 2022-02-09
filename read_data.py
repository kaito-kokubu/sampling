import signal
import time
from Subfact_ina219 import INA219
import ina219_example
import led

first_exec_time = 1 #1回目の実行までの時間 (s)
interval = 1 #2回目以降の実行間隔 (s)
read_data_time = 120 #計測時間 (s)

led.led_start(read_data_time)

def scheduler(ina):
    ina219_example.main(ina)

signal.signal(signal.SIGALRM, scheduler)
signal.setitimer(signal.ITIMER_REAL, first_exec_time, interval)

ina = INA219()

time.sleep(read_data_time)