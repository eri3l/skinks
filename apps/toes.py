# -*- coding: utf-8 -*-

"""
re-do streamlit with: 
    a. Toes, SVL, Traplists
    b. Toes
"""
import pandas as pd
import numpy as np
import streamlit as st
import itertools
#import pickle5 as pickle	# for python 3.7 

from itertools import chain

def app():
    st.title("Search by missing toes only")
    #--- 1. Load data
    def load_file(filename):
        
        df = pd.read_csv(filename, converters={'Trap': eval, 'Toes':eval})
        df['Sex'] = df['Sex'].astype(str)

        return df 
    
    df = load_file("source02.csv")
    
    #--- 2. Create filter options
    
    vals = np.unique([*itertools.chain.from_iterable(df.Toes)]) # get all unique toes from df.Toes
    toes_choice = st.sidebar.multiselect("Select or type missing toes: ", vals)     # list 
    
    
    #--- 3. Search
    #----- testcases
    # trap_choice = ['R66', 'board', 'R67', 'M14', 'R68', 'R69', 'R70', 'M11', 'PR1']  # list
    # toes_choice = ['LF1']   # list
    # toes_ch = []        # list  for intact
    
    
    newdf = df.loc[df['Toes'].apply(lambda x: len(set(x) - set(toes_choice)) == 0)]
                  
    
    newdf['toes_len'] = newdf.Toes.apply(len)
    newdf = newdf.sort_values(by='toes_len', ascending=False).drop(columns='toes_len')
    #-- optional: remove all rows with *intact* toes
    newdf = newdf[newdf['Toes'].map(len) != 0]
    
    # get all with missing toes -->  df.Toes.apply(lambda x: len(x)!=0) 
    # or df['Toes'].map(len)!=0
    
    
    st.write(" `SEARCH RESULTS` ")    
    st.table(newdf)




