# -*- coding: utf-8 -*-
"""
File to download zip files from internet
Created on Wed Oct 15 21:03:00 2014

@author: Ralf Becker
"""

# tes

from time import time
import urllib.request
#import subprocess

target = "http://www.nemweb.com.au/REPORTS/CURRENT/Yesterdays_Bids_Reports/PUBLIC_YESTBID_201408170000_20140818040531.zip" # change this to a more useful URL

#wget_start = time()
#
#proc = subprocess.Popen(["wget", target])
#proc.communicate()
#
#wget_end = time()


url_start = time()
test = urllib.request.urlretrieve(target, 'testtest.zip')
url_end = time()

#print('wget -> {0:6.4f}'.format((wget_end - wget_start)))
print('urllib.urlretrieve -> {0:6.4f}'.format((url_end - url_start)))
