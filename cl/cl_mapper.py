#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Assuming tab-separated values
    location = fields[5]
    if location:  # 
        print(f"{location}\t1")  # Emit (LOCATION	1)
