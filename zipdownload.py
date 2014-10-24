# -*- coding: utf-8 -*-
"""
File to download zip files from internet
Created on Wed Oct 15 21:03:00 2014

@author: Ralf Becker
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 21:49:41 2014

@author: kpetruskevicius
"""
import os
import urllib
from zipfile import *
import urllib2
from bs4 import BeautifulSoup
downloads = []
url = 'http://www.nemweb.com.au/REPORTS/CURRENT/Yesterdays_Bids_Reports/'
list_of_links = []
conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html)
links = soup.find_all('a')
for tag in links:
    link = tag.get('href',None)
    if link != None:
        if link not in list_of_links:
            list_of_links.append("http://www.nemweb.com.au" + link)
print list_of_links

from time import time
#import subprocess

target = list_of_links # list of links to zip files
targeturl = urllib.URLopener()
#
#proc = subprocess.Popen(["wget", target])
#proc.communicate()
#

url_start = time() #wget_start = time()
for links in target:
    if links != 'http://www.nemweb.com.au/REPORTS/CURRENT/':
        if links not in downloads:
            print downloads
            targeturl.retrieve(links, links[80:])
            downloads.append(links)
            link = links[80:]
            downloads.append(links)
            zipf = zipfile.ZipFile(links[80:],"r")
            zipf.extractall("/Users/kpetruskevicius/Documents/datasquad/AUSelec_bids/unzipped/")
            print links[80:] + " downloaded"
    else:
        print ""
url_end = time() #wget_end = time()

#print('wget -> {0:6.4f}'.format((wget_end - wget_start)))
print('urllib.urlretrieve -> {0:6.4f}'.format((url_end - url_start)))
