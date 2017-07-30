# -*- coding: utf-8 -*-
"""
Looks for daily zip files and extracts csv
@author: Ralf Becker
"""
# -*- coding: utf-8 -*-

import os
import zipfile

list_of_links = [] #empty list

os.chdir('O:\\elec\\AEMO_DVD\\Bid Files\\2013')   

subdi = os.listdir(os.getcwd())

for i in subdi:
    subdi2 = os.getcwd() + '\\' + i
    os.chdir(subdi2)  

    downloads = os.listdir(os.getcwd()) #creating a list of files in the current directory
    for item in downloads:
        if '.zip' in item:
            if 'PUBLIC_YESTBID' in item:  # to eliminate monthly zip files
                                #extracting csv from zip and leave in specified folder
                zipfile.ZipFile(item,"r").extractall('O:\\elec\\bids\\data') 
                print item + " unzipped"


    os.chdir('O:\\elec\\AEMO_DVD\\Bid Files\\2013')   # get beck to root


#downloads = os.listdir(os.getcwd()) #creating a list of files in the current directory
#print downloads # printing all the files
#
#for item in downloads:
#    if '.zip' in item:
#        if 'PUBLIC_YESTBID' in item:  # to eliminate monthly zip files
#            if item[:-3]+"csv" not in downloads: # check whether csv already exists
#                ZipFile(item,"r").extractall(os.getcwd()) #extracting csv from zip
#                print item + " unzipped"
#
