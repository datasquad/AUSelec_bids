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
date = []
def splitter(source,prices,quantities):
    for line in source:
        if "C" in line:
            date.append(line[5:6])
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
gen_names.remove("W/HOE#1")
gen_names.remove("W/HOE#2")
#readerprices = csv.reader(open("prices.CSV","rb"), delimiter=',')
#readerquantities = csv.reader(open("quantities.CSV","rb"), delimiter=',')
#print readerprices
dater = str(date)
datef = dater[3:7] + "_" + dater[8:10] + "_"+ dater[11:13]
def qtwriter(ui,uv,up):
    for mn in ui:
        if uv == mn[5]:
            up.writerow(mn)
for i in gen_names:
    readerprices = csv.reader(open("prices.CSV","rb"), delimiter=',')
    readerquantities = csv.reader(open("quantities.CSV","rb"), delimiter=',')
    g =  str(i) + "_" + datef + ".CSV"
    p = csv.writer(open(g,"wa"))
    readerprices = csv.reader(open("prices.CSV","rb"), delimiter=',')
    readerquantities = csv.reader(open("quantities.CSV","rb"), delimiter=',')
    qtwriter(readerprices,i,p)
    qtwriter(readerquantities,i,p)
    #for t in readerprices:
      #  if i == t[5]:
           # print t
        #    p.writerow(t)
    #for x in readerquantities:
       # if i == x[5]:
        #    p.writerow(x)
       # print x

"""print gen_names
print data"""
