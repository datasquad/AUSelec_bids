# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 02:49:53 2014

@author: kpetruskevicius
"""
import csv

reader = csv.reader(open("info.CSV", "rb"), delimiter=',')
f = csv.writer(open("karolis.CSV", "wb"))
c = csv.writer(open("quantities.CSV", "wb"))
for line in reader:
    if "C" in line:
        date = line[5:6]
        print date
    elif "I" in line and "REBIDEXPLANATION" in line:
        line[3] = "AEMO"
        f.writerow(line)
    elif "ENERGY" in line:
            f.writerow(line)
    else:
        if "I" in line and "ROCUP" in line:
            break
            
import pandas
data = pandas.read_csv('karolis.CSV')
print data