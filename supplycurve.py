
"""
Created on Fri Jan 9 2015

Uploads generator/day specific data from 

DUID_q/p_YYYralffbeckerY_MM_DD.csv
where DUID is the generator code

and generates supply curves

@author: ralffbecker
"""

import csv
import os
import numpy as np
import pandas as pd

path = "O://elec//bids//gen_date_data//"
folder = os.listdir(path) #retrieves a list of files in relevant directory

# Selection criteria
filter_DUID = "BRAEMAR2"
filter_YYYY = "2013"
filter_MM   = "11"
filter_DD   = "03"

for fn in folder: # looping through every name in the list
    if filter_DUID in fn and filter_YYYY in fn and filter_MM in fn and filter_DD in fn: # checking if it's one of the required files
        
        if "_q_" in fn: # the quantity information
            q_df = pd.read_csv(path+fn)
            duid = fn[:fn.find("_q_")] # add DUID code to dataframe
            q_df['DUID'] = duid
                # change dates to datetime format
            q_df['LASTCHANGED'] = pd.to_datetime(q_df['LASTCHANGED'])
            q_df['SETTLEMENTDATE'] = pd.to_datetime(q_df['SETTLEMENTDATE'])
            q_df['BIDSETTLEMENTDATE'] = pd.to_datetime(q_df['BIDSETTLEMENTDATE'])            
            q_df['BIDOFFERDATE'] = pd.to_datetime(q_df['BIDOFFERDATE'])
            q_df['SETTLEMENTDATE'] = pd.to_datetime(q_df['SETTLEMENTDATE'])
            q_df['BIDSETTLEMENTDATE'] = pd.to_datetime(q_df['BIDSETTLEMENTDATE'])            
            test = 2
             
        
        elif "_p_" in fn: # the price information
            p_df = pd.read_csv(path+fn)
            duid = fn[:fn.find("_p_")] # add DUID code to dataframe
            p_df['DUID'] = duid

                # change dates to datetime format
            p_df['LASTCHANGED'] = pd.to_datetime(p_df['LASTCHANGED'])
            p_df['SETTLEMENTDATE'] = pd.to_datetime(p_df['SETTLEMENTDATE'])
            p_df['BIDSETTLEMENTDATE'] = pd.to_datetime(p_df['BIDSETTLEMENTDATE'])            
            p_df['BIDOFFERDATE'] = pd.to_datetime(p_df['BIDOFFERDATE'])
            p_df['SETTLEMENTDATE'] = pd.to_datetime(p_df['SETTLEMENTDATE'])
            p_df['BIDSETTLEMENTDATE'] = pd.to_datetime(p_df['BIDSETTLEMENTDATE'])            
            p_df['FIRSTDISPATCH'] = pd.to_datetime(p_df['FIRSTDISPATCH']) 
            p_df['FIRSTPREDISPATCH'] = pd.to_datetime(p_df['FIRSTPREDISPATCH']) 
            test = 3


# find the bidversions

[bids_times,bids_index] = np.unique(p_df.loc[:,'LASTCHANGED'],return_index=True)    # find unique (re)bid times
bids = p_df.loc[bids_index,'BIDVERSIONNO'].values                                   # returns bidversion no in their right order
ns = bids.size 

price_cols = ['PRICEBAND1','PRICEBAND2','PRICEBAND3','PRICEBAND4','PRICEBAND5',
                  'PRICEBAND6','PRICEBAND7','PRICEBAND8','PRICEBAND9','PRICEBAND10']

quant_cols = ['BANDAVAIL1','BANDAVAIL2','BANDAVAIL3','BANDAVAIL4','BANDAVAIL5',
                  'BANDAVAIL6','BANDAVAIL7','BANDAVAIL8','BANDAVAIL9','BANDAVAIL10','PERIODID','MAXAVAIL']

for i in range(ns):
    p_temp = p_df.ix[p_df.ix[:,'BIDVERSIONNO']==(bids[i]),price_cols].values
    q_temp = q_df.ix[q_df.ix[:,'BIDVERSIONNO']==(bids[i]),quant_cols].values

    test = 3    

# so far code assumes that we are only uploading one file
# to add: 
# - allow for aggregation across several generators
