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
def splitter(source,prices,quantities):
    for line in source:
        if "C" in line:
            date = line[5:6]
            print date
        elif line[3] == "5" and line[6] == "ENERGY" or "I" in line and line[3] == "5":
            prices.writerow(line)
        elif line[3] == "3" and line[6] == "ENERGY" or "I" in line and line[3] == "3":
            quantities.writerow(line)
splitter(reader,f,c)
data = pandas.read_csv('quantities.CSV')
print data