#!/bin/bash

top -b -d 0.1 -n 140 | python top_analysis.py > top_result.txt