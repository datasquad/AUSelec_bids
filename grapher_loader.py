# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:45:20 2014

@author: kpetruskevicius
"""

import os
import pandas
import numpy as np
import matplotlib.pyplot as plt #http://matplotlib.org/users/pyplot_tutorial.html
folder = os.listdir(os.getcwd()) #get the list of files in the current working directory

def loader(name,date):
    for i in folder: #loop through the list of files in the folder
        if name in i and date in i and "p" in i:
            loader.prices = pandas.read_csv(i) #loading price csv into pandas dataframes
        if name in i and date in i and "q" in i:
            loader.quantity = pandas.read_csv(i) #loading quanitity csv into pandas dataframes


loader("VP5","2014_09_29") #choosing calues required
q0 = loader.quantity.loc[0,'BANDAVAIL1':'BANDAVAIL10'] #defining values required to use .loc[index,column]
p = loader.prices.loc[0,'PRICEBAND1':'PRICEBAND10'] #defining values required to use .loc[index,column]
q1 = loader.quantity.loc[30,'BANDAVAIL1':'BANDAVAIL10'] #defining values required to use .loc[index,column]

plt.plot(q0, p, "r--", q1, p, "b-") #plotting graphs (x,y,type,x1,x2,type2)
plt.show()
