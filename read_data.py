import smbus
import time
from datetime import datetime
import signal

i2c = smbus.SMBus(1)
addr = 0x40

data = i2c.read_byte_data(addr, 0x05)
print(data)


