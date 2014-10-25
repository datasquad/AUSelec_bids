# -*- coding: utf-8 -*-
"""
File to download zip files from internet
Created on Wed Oct 15 21:03:00 2014

@author: Ralf Becker
"""
# -*- coding: utf-8 -*-

import os
import urllib
from zipfile import *
import urllib2
from bs4 import BeautifulSoup
from time import time #import subprocess
list_of_links = [] #empty list
downloads = os.listdir(os.getcwd()) #creating a list of files in the current directory
print downloads # printing all the files
url = 'http://www.nemweb.com.au/REPORTS/CURRENT/Yesterdays_Bids_Reports/' #url path to the main website
conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html)
links = soup.find_all('a') #find all links
""" Creating a list of links to look through"""
for tag in links:
    link = tag.get('href',None)
    if link != None:
        if link not in list_of_links:
            list_of_links.append("http://www.nemweb.com.au" + link)

target = list_of_links # list of links to zip files
targeturl = urllib.URLopener() #url opener
#
#proc = subprocess.Popen(["wget", target])
#proc.communicate()
#
url_start = time() #wget_start = time()
"""Downloading zip files from the website, checking if they aren't 
already on the computer and extracting them to a new folder unzippe 
for this step to work you need to make sure to create a new folder unzipped and
specify your path to this folder. Instead of kpetruskevicius you will have your
own folder. I think we'll need to try and figure out a way to make it universal
at some point """

for links in target: 
    if links != 'http://www.nemweb.com.au/REPORTS/CURRENT/':
        #link = links[80:links[80:].index(.)] # could figure out a way to store
    #then could delete the zip files of the machine
        if links[80:] not in downloads:
            targeturl.retrieve(links, links[80:]) # zip file download
            ZipFile(links[80:],"r").extractall(os.getcwd()) #extracting csv from zip
            #os.remove(links[80:]) #removing file from computer
            print links[80:] + " downloaded"
            
    else:
        print ""
url_end = time() #wget_end = time()
#print('wget -> {0:6.4f}'.format((wget_end - wget_start)))
print('urllib.urlretrieve -> {0:6.4f}'.format((url_end - url_start)))


