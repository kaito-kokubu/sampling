#!/usr/bin/python

from Subfact_ina219 import INA219
import datetime

def main():
    ina = INA219()
    shunt = ina.getShuntVoltage_mV()
    bus = ina.getBusVoltage_V()
    current = ina.getCurrent_mA()

    print("Shunt   : %.3f mV" % shunt)
    print("Bus     : %.3f V" % bus)
    print("Current : %.3f mA" % current)

    return [datetime.datetime.now(), shunt, bus, current]

if __name__ == '__main__':
    main()