#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Data is tab-separated
    date_occ = fields[2]  # 'DATE OCC' column (Index 2 based on sample data)
    if date_occ:  # Ignore empty values
	date_split = date_occ.split(" ") # remove the timestamp part from the date by splitting
	date_arr = date_split[0].split("/") #split by month date and year MM/DD/YYYY
	month_year = str(date_arr[0]) + '/' + str(date_arr[2]) # get just the date part
        print(f"{month_year}\t1")
