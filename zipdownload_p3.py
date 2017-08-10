# -*- coding: utf-8 -*-
"""
This is to download zip files from a web directory
Author: Ralf Becker
"""
import os
import requests
import urllib
from zipfile import *
from bs4 import BeautifulSoup


list_of_links = [] #empty list
downloads = os.listdir(os.getcwd()) #creating a list of files in the current directory

page = requests.get("http://www.nemweb.com.au/REPORTS/ARCHIVE/Yesterdays_Bids_Reports/")
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('a') #find all links
""" Creating a list of links to look through"""
for tag in links:
    link = tag.get('href',None)
    if link != None:
        if link not in list_of_links:
            list_of_links.append("http://www.nemweb.com.au" + link)
            
target = list_of_links[2:] # deletes first link that merely points back to parent directory  
targeturl = urllib.request.URLopener() #url opener

for links in target: 
    temp_link = links[65:]

    if temp_link not in downloads:
        targeturl.retrieve(links, temp_link) # zip file download
        ZipFile(temp_link,"r").extractall(os.getcwd()+"\\extractedYESTBIDS") #extracting csv from zip
        #os.remove(links[80:]) #removing file from computer
        print(temp_link + " downloaded")
            