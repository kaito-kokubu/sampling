#!/bin/bash

date_today=`date +%Y%m%d%H%M`

echo `date "+%Y-%m-%d %H:%M:%S"` >> ./result/ina219_$date_today.csv

./build/profiler -p >> ./result/ina219_$date_today.csv
