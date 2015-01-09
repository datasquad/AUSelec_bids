
"""
Created on Wed Oct 29 02:49:53 2014

This file creates Generator and day specific files with quantitty and price data:
The data source is the PUBLIC_YESTBID_*.csv files
The name structure of the csv files is as follows:

DUID_q/p_YYYY_MM_DD.csv

where DUID is the generator code

@author: kpetruskevicius
"""
import csv
import os
def splitter(source):
    gfd = csv.reader(open(source, "rb"), delimiter=',')
    f = csv.writer(open("prices.CSV", "wb"))
    c = csv.writer(open("quantities.CSV", "wb"))
    ind = 0
    for line in gfd:
        
        if line[0] == "I":
            ind = ind + 1 #counting instances of "I" as the first value in the line

        if "C" in line:
            date.append(line[5:6]) #saving date of the main file
        elif (line[6] == "ENERGY") or (line[6] == "BIDTYPE"):
            if ind == 1:  # price file
                f.writerow(line) #writing prices
                if line[5] not in gen_names:
                    gen_names.append(line[5])
            else:         # quantity file
                c.writerow(line) #writing quantities
                

def linewriter(sourcesub,gennamesub,outputsub): 
    for mn in sourcesub: #looping through the source file
        if (gennamesub == mn[5]) or ("I" == mn[0]): # select if generator match or heading line
            outputsub.writerow(mn) #write a line if the gen_name is as selected to output file.

folder = os.listdir(os.getcwd()) #retrieves a list of files in current working directory
for filename in folder: # looping through every name in the list
    if "PUBLIC_YESTBID" in filename and ".CSV" in filename: # checking if it's one of the daily files
        gen_names = [] #creating empty list
        date = [] #creating empty list
        splitter(filename) #running the CSV file through the splitter method
        gen_names.remove("DUID") # removing DUID value from the list of the generator names. This is created in splitters method
        dater = str(date) #converting the date into a string
        datef = dater[3:7] + "_" + dater[8:10] + "_"+ dater[11:13] #picking out relevant date parts
        for i in gen_names: #looping through generator names list without "DUID"
            if "/" in i: #checking if the generator name does not have any of the prohibited characters.
                i = i.replace("/",'') #if they do simply changing the name of the generator. Replacing prohibited character with nothing.
            readerprices = csv.reader(open("prices.CSV","rb"), delimiter=',') #opening prices.csv created in splitter method
            readerquantities = csv.reader(open("quantities.CSV","rb"), delimiter=',') #opening quantities.csv created by splitter method
            g =  str(i) + "_p_" + datef + ".CSV" #creating a string which will be a name for a price file of the generator.
            gq = str(i) + "_q_" + datef + ".CSV" #creating a string which will be a name for a quantity file of the generator.
            p = csv.writer(open(g,"wb")) #creating file for prices
            pq = csv.writer(open(gq,"wb")) #creatinf file for quantities
            readerprices = csv.reader(open("prices.CSV","rb"), delimiter=',') #reading main file
            readerquantities = csv.reader(open("quantities.CSV","rb"), delimiter=',') #reading main file
            linewriter(readerprices,i,p) #using method linewriter
            linewriter(readerquantities,i,pq) #using method line writer


