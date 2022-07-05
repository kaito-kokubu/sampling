#!/bin/bash

echo `date "+%Y-%m-%d %H:%M:%S"`

./build/profiler -p >> ./result/ina219_$(date +%Y%m%d%H%M).csv
