#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Assuming tab-separated values

    vict_age = fields[11]  # Vict Age
    crime_type = fields[9]  # Crm Cd Desc (Crime Type)

    # Categorize victim age into age groups
    try:
        age = int(vict_age)
        if age < 18:
            age_group = "Under_18"
        elif age < 35:
            age_group = "18_34"
        elif age < 60:
            age_group = "35_59"
        else:
            age_group = "60_plus"
    except ValueError:
        age_group = "Unknown"

    # Emit key-value pair (Crime Type, Age Group)
    if crime_type and crime_type != "Crm Cd Desc":
        print(f"{crime_type}|{age_group}\t1")
