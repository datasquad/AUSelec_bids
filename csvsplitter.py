
"""
Created on Wed Oct 29 02:49:53 2014

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
            ind = ind + 1

        if "C" in line:
            date.append(line[5:6])
        elif (line[6] == "ENERGY") or (line[6] == "BIDTYPE"):
            if ind == 1:  # price file
                f.writerow(line)
                if line[5] not in gen_names:
                    gen_names.append(line[5])
            else:         # quantity file
                c.writerow(line)
                

def qtwriter(ui,uv,up):
    for mn in ui:
        if (uv == mn[5]) or ("I" == mn[0]): # select if generator match or heading line
            up.writerow(mn)

folder = os.listdir(os.getcwd())
for filename in folder:
    if "PUBLIC_YESTBID" in filename and ".CSV" in filename:
        gen_names = []
        date = []

        opf=filename
        splitter(opf)
        gen_names.remove("DUID")
        dater = str(date)
        datef = dater[3:7] + "_" + dater[8:10] + "_"+ dater[11:13]
        for i in gen_names:
            if "/" in i:
                i = i.replace("/",'')
            readerprices = csv.reader(open("prices.CSV","rb"), delimiter=',')
            readerquantities = csv.reader(open("quantities.CSV","rb"), delimiter=',')
            kl = str(i) + "_" + datef
            g =  str(i) + "_p_" + datef + ".CSV"
            gq = str(i) + "_q_" + datef + ".CSV"
            p = csv.writer(open(g,"wb"))
            pq = csv.writer(open(gq,"wb"))
            readerprices = csv.reader(open("prices.CSV","rb"), delimiter=',')
            readerquantities = csv.reader(open("quantities.CSV","rb"), delimiter=',')
            qtwriter(readerprices,i,p)
            qtwriter(readerquantities,i,pq)


