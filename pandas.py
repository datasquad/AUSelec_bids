# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 02:49:53 2014

@author: kpetruskevicius
"""
import csv
import os
import urllib
from zipfile import *
import urllib2
from bs4 import BeautifulSoup
from time import time #import subprocess

reader = csv.reader(open("info.CSV", "rb"), delimiter=',')
p = csv.writer(open("karolis.CSV", "wb"))
for line in reader:
    if "C" in line:
        date = line[5:6]
        print date
    elif "I" in line:
        line[3] = "AEMO"
        f.writerow(line)
    else:
        if "ENERGY" in line:
            f.writerow(line)
            
import pandas
data = pandas.read_csv('karolis.CSV')
print data