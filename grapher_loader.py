# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:45:20 2014

@author: kpetruskevicius
"""

import os
import pandas
import numpy as np
import matplotlib.pyplot as plt #http://matplotlib.org/users/pyplot_tutorial.html
folder = os.listdir(os.getcwd())

def loader(name,date):
    for i in folder:
        if name in i and date in i and "p" in i:
            loader.prices = pandas.read_csv(i)
        if name in i and date in i and "q" in i:
            loader.quantity = pandas.read_csv(i)


loader("TRIBUTE","2014_09_01")
q0 = loader.quantity.loc[0,'BANDAVAIL1':'BANDAVAIL10']
p = loader.prices.loc[0,'PRICEBAND1':'PRICEBAND10']
q1 = loader.quantity.loc[30,'BANDAVAIL1':'BANDAVAIL10']

plt.plot(q0, p, "r--", q1, p, "b-")
plt.show()
