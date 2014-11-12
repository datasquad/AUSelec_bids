# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 02:49:53 2014

@author: kpetruskevicius
"""
import csv
import pandas

reader = csv.reader(open("info.CSV", "rb"), delimiter=',')
f = csv.writer(open("prices.CSV", "wb"))
c = csv.writer(open("quantities.CSV", "wb"))
for line in reader:
    if "C" in line and "AEMO" in line:
        date = line[5:6]
        print date
    elif line[3] == 5:
        f.writerow(line)
    elif line[3] == 3:
        c.writerow(line)
    else:
        break

data = pandas.read_csv('prices.CSV')
print data