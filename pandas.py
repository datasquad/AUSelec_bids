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
gen_names = []
def splitter(source,prices,quantities):
    for line in source:
        if "C" in line:
            date = line[5:6]
            print date
        elif line[3] == "5" and line[6] == "ENERGY" or "I" in line and line[3] == "5":
            prices.writerow(line)
            if line[5] not in gen_names:
                gen_names.append(line[5])
        elif line[3] == "3" and line[6] == "ENERGY" or "I" in line and line[3] == "3":
            quantities.writerow(line)
splitter(reader,f,c)
"""def generatornames(source):
    for line in source:
        if line[0] ==  "D":
            if line[5] not in gen_names:
                gen_names.append(line[5])

g = csv.reader(open("prices.csv","rb"))
generatornames(g)"""
data = pandas.read_csv('prices.CSV')
gen_names.remove("DUID")
print data
print gen_names