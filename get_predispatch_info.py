# -*- coding: utf-8 -*-
"""
This is to download information from predispatch files which are in double zip files
and then in csv files
Then we extract the predispatch inf we want from these
Author: Ralf Becker
"""
import os
import requests
import urllib
from zipfile import *
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy as np

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
            
           temp = pd.read_csv("E:\\elec\\data\\PreDispatch\\test\\temp\\"+link3,skiprows=1)
           temp2 = temp.loc[lambda temp: temp.PRICESENSITIVITIES == "PRICESENSITIVITIES", :]
                   # separate into states
           temp2_NSW = temp2.loc[lambda temp2: (temp2.REGIONID == "NSW1"), :]
           temp2_QLD = temp2.loc[lambda temp2: (temp2.REGIONID == "QLD1"), :]
           temp2_SA  = temp2.loc[lambda temp2: (temp2.REGIONID == "SA1"), :]
           temp2_VIC = temp2.loc[lambda temp2: (temp2.REGIONID == "VIC1"), :]
           temp2_TAS = temp2.loc[lambda temp2: (temp2.REGIONID == "TAS1"), :]

                   # ensure that the periods are ordered correctly
           temp2_NSW = temp2_NSW.iloc[np.argsort(temp2_NSW.PERIODID.astype(int).values)]  # sort by PERIODID which has to be forced to be an integer
           temp2_QLD = temp2_QLD.iloc[np.argsort(temp2_QLD.PERIODID.astype(int).values)]  # sort by PERIODID which has to be forced to be an integer
           temp2_SA  = temp2_SA.iloc[np.argsort(temp2_SA.PERIODID.astype(int).values)]  # sort by PERIODID which has to be forced to be an integer
           temp2_VIC = temp2_VIC.iloc[np.argsort(temp2_VIC.PERIODID.astype(int).values)]  # sort by PERIODID which has to be forced to be an integer
           temp2_TAS = temp2_TAS.iloc[np.argsort(temp2_TAS.PERIODID.astype(int).values)]  # sort by PERIODID which has to be forced to be an integer
           

                    # separate into scenarios 
           temp2_1_NSW  = temp2_NSW[['LASTCHANGED','DATETIME','RRPEEP1']]
           temp2_2_NSW  = temp2_NSW[['LASTCHANGED','DATETIME','RRPEEP2']]
           temp2_3_NSW  = temp2_NSW[['LASTCHANGED','DATETIME','RRPEEP3']]
           temp2_4_NSW  = temp2_NSW[['LASTCHANGED','DATETIME','RRPEEP4']]
           temp2_5_NSW  = temp2_NSW[['LASTCHANGED','DATETIME','RRPEEP5']]
           temp2_6_NSW  = temp2_NSW[['LASTCHANGED','DATETIME','RRPEEP6']]
           temp2_7_NSW  = temp2_NSW[['LASTCHANGED','DATETIME','RRPEEP7']]
           temp2_8_VIC  = temp2_VIC[['LASTCHANGED','DATETIME','RRPEEP8']]
           temp2_9_VIC  = temp2_VIC[['LASTCHANGED','DATETIME','RRPEEP9']]
           temp2_10_VIC = temp2_VIC[['LASTCHANGED','DATETIME','RRPEEP10']]
           temp2_11_VIC = temp2_VIC[['LASTCHANGED','DATETIME','RRPEEP11']]
           temp2_12_VIC = temp2_VIC[['LASTCHANGED','DATETIME','RRPEEP12']]
           temp2_13_VIC = temp2_VIC[['LASTCHANGED','DATETIME','RRPEEP13']]
           temp2_14_VIC = temp2_VIC[['LASTCHANGED','DATETIME','RRPEEP14']]        
           temp2_15_SA   = temp2_SA[['LASTCHANGED','DATETIME','RRPEEP15']]
           temp2_16_SA   = temp2_SA[['LASTCHANGED','DATETIME','RRPEEP16']]
           temp2_17_SA   = temp2_SA[['LASTCHANGED','DATETIME','RRPEEP17']]
           temp2_18_SA   = temp2_SA[['LASTCHANGED','DATETIME','RRPEEP18']]
           temp2_19_SA   = temp2_SA[['LASTCHANGED','DATETIME','RRPEEP19']]
           temp2_20_SA   = temp2_SA[['LASTCHANGED','DATETIME','RRPEEP20']]
           temp2_43_SA   = temp2_SA[['LASTCHANGED','DATETIME','RRPEEP43']]
           temp2_29_QLD  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP29']]        
           temp2_30_QLD  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP30']]        
           temp2_31_QLD  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP31']]        
           temp2_32_QLD  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP32']]
           temp2_33_QLD  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP33']]        
           temp2_34_QLD  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP34']]        
           temp2_35_QLD  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP35']]                   
           temp2_36_TAS  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP29']]        
           temp2_37_TAS  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP30']]        
           temp2_38_TAS  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP31']]        
           temp2_39_TAS  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP32']]
           temp2_40_TAS  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP33']]        
           temp2_41_TAS  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP34']]        
           temp2_42_TAS  = temp2_QLD[['LASTCHANGED','DATETIME','RRPEEP35']]                              