#!/usr/bin/python

#from operator import itemgetter
import sys

last_Vict_Sex = None
total_count = 0

for line in sys.stdin:
    line = line.strip()

    Vict_Sex, count = line.split("\t")
    count = int(count)

    if not Vict_Sex:
        last_Vict_Sex = Vict_Sex

    if Vict_Sex == last_Vict_Sex:
        total_count +=  count
    else:
        result = [last_Vict_Sex, total_count]
        print ("\t".join(str(v) for v in result))
        last_Vict_Sex = Vict_Sex
        total_count = 1
    
print ("\t".join(str(v) for v in [last_Vict_Sex, total_count]))
