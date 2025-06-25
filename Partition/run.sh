#!/bin/bash

if [ -f partition_performance.csv ]; then
    rm partition.csv
fi
python3 main.py
 