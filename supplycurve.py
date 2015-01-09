
"""
Created on Fri Jan 9 2015

Uploads generator/day specific data from 

DUID_q/p_YYYralffbeckerY_MM_DD.csv
where DUID is the generator code

and generates supply curves

@author: ralffbecker
"""

import os
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from pylab import *
from matplotlib.collections import LineCollection


def plot_supply(in_p, in_q, pr = 0):
    # this function plots a supply curve
    # input: (i) array with ordered price bands, (one dimensional array)
    #        (ii) array with ordered quantities to price bands
    #        (iii) pr = 0 no print, = 1 print
    # output: (i) temp_p, price vector used for printing
    #         (ii) temp_q, quantity vector used for printing
    # @author: ralffbecker

    
    if in_p.size != in_q.size:
        print("Price and quantity input need to have same length")
    
    k = in_p.size  # number of price bands

    # create points for stepfunction

    in_q = np.cumsum(in_q)
    
    temp_p = np.zeros(2*k)    
    temp_q = np.zeros(2*k)
    temp_p[0] = in_p[0]
    temp_p[1] = in_p[0]     # first two points are (p1,0), (p1,q1)
    temp_q[1] = in_q[0] 
    i_p = 0                 # index for next price
    i_q = 0                 # index for next quantity
    for i in range(2,2*k):
        if np.mod(i,2) != 0:
            i_q = i_q + 1
        else:
            i_p = i_p + 1
        
        temp_p[i] = in_p[i_p] 
        temp_q[i] = in_q[i_q]         
        
    if pr:
        fig1 = plt.figure()
        plt.plot(temp_q,temp_p)
        plt.xlabel('Quantity')
        plt.ylabel('Price')
        plt.title('Electricity Supply Curve',fontsize=20)
        plt.show()
    
    return temp_p,temp_q    
    

path = "O://elec//bids//gen_date_data//"
folder = os.listdir(path) #retrieves a list of files in relevant directory

# Selection criteria
filter_DUID = "GORDON"
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

periodid = 15   # choose the period of the day

p_coll = range(20)
q_coll = range(20)

for i in range(ns):
    p_in = p_df.ix[p_df.ix[:,'BIDVERSIONNO']==(bids[i]),price_cols].values
    q_in = q_df.ix[q_df.ix[:,'BIDVERSIONNO']==(bids[i]),quant_cols].values

    [p_temp,q_temp] = plot_supply(p_in.T,q_in[periodid,0:10],0)
    p_coll = np.vstack((p_coll,p_temp))
    q_coll = np.vstack((q_coll,q_temp))

p_coll = p_coll[1:,:]
q_coll = q_coll[1:,:]    

# We need to set the plot limits, they will not autoscale
# check http://matplotlib.org/1.4.2/examples/pylab_examples/line_collection2.html
ax = axes()
ax.set_xlim((amin(q_coll),amax(q_coll)))
ax.set_ylim((amin(p_coll),amax(p_coll)))

# so far code assumes that we are only uploading one file
# to add: 
# - allow for aggregation across several generators
