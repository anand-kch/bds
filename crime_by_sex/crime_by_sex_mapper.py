#! /usr/bin/python

import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    unpacked = line.split (",")
    DR_NO, Date_Rptd, DATE_OCC, TIME_OCC, AREA, AREA_NAME, Rpt_Dist_No, Part_1-2, Crm_Cd, Crm_Cd_Desc, Mocodes, Vict_Age, Vict_Sex, Vict_Descent, Premis_Cd, Premis_Desc, Weapon_Used_Cd, Weapon_Desc, Status, Status_Desc, Crm_Cd_1, Crm_Cd_2, Crm_Cd_3, Crm_Cd_4, LOCATION, Cross_Street, LAT, LON  = line.split (",")
    #print (unpacked)
    #print (Vict_Sex)
    #print (Crm_Cd_Desc)
    result = [Vict_Sex, 1]
    #print (result)