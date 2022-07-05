#!/bin/bash

start_time=`date "+%Y-%m-%d %H:%M:%S"`

./build/profiler -p >> ./result/ina219_$(date +%Y%m%d%H%M).csv

end_time=`date "+%Y-%m-%d %H:%M:%S"`

echo $start_time
echo $end_time