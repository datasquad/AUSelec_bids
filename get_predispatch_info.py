# -*- coding: utf-8 -*-
"""
This is to download information from predispatch files
Author: Ralf Becker
"""
import os
import requests
import urllib
from zipfile import *
from bs4 import BeautifulSoup
import csv

# this assumes that weekly sensitivty files are in test folder

list_of_links = [] #empty list
downloads = os.listdir("E:\\elec\\data\\PreDispatch\\test") #creating a list of files in the current directory


for link in downloads:

    ZipFile("E:\\elec\\data\\PreDispatch\\test\\"+link,"r").extractall("E:\\elec\\data\\PreDispatch\\test\\temp") #extracting csv from zip
#    os.remove("E:\\elec\\data\\PreDispatch\\test\\"+link) #removing file from computer
    print(link + " extracted to temp")
    
    # now we have the individual half hourly predispatch files in temp
    downloads2 = os.listdir("E:\\elec\\data\\PreDispatch\\test\\temp") #creating a list of files in the current directory
    
    for link2 in downloads2[1:2]:    
        ZipFile("E:\\elec\\data\\PreDispatch\\test\\temp\\"+link2,"r").extractall("E:\\elec\\data\\PreDispatch\\test\\temp") #extracting csv from zip
#       os.remove("E:\\elec\\data\\PreDispatch\\test\\"+link) #removing file from computer

        downloads3 = os.listdir("E:\\elec\\data\\PreDispatch\\test\\temp") #creating a list of files in the current directory
        downloads3 = [name for name in downloads3 if '.CSV' in name]   # this is using list comprehension
        
        for link3 in downloads3:  # now we handle the csv files
            
            with open("E:\\elec\\data\\PreDispatch\\test\\temp\\"+link3) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['first_name'], row['last_name'])

        
        