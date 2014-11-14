# -*- coding: utf-8 -*-
"""
Looks for daily zip files and extracts csv
@author: Ralf Becker
"""
# -*- coding: utf-8 -*-

import os

list_of_links = [] #empty list
downloads = os.listdir(os.getcwd()) #creating a list of files in the current directory
print downloads # printing all the files

for item in downloads:
    if '.zip' in item:
        if 'PUBLIC_YESTBID' in item:  # to eliminate monthly zip files
            if item[:-3]+"csv" not in downloads: # check whether csv already exists
                ZipFile(item,"r").extractall(os.getcwd()) #extracting csv from zip
                print item + " unzipped"

