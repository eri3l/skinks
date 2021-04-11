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

from itertools import chain

def app():
    st.write("""## Search by missing toes only""")
    
    #--- 1. Load data
    def load_file(filename):
        
        df = pd.read_csv(filename, converters={'Trap': eval, 'Toes':eval})
        df['Sex'] = df['Sex'].astype(str)
    
        return df 
    
    df = load_file("data/source10Apr20_02.csv")
    
    #--- 2. Create filter options
    
    vals = np.unique([*itertools.chain.from_iterable(df.Toes)]) # get all unique toes from df.Toes
    toes_choice = st.multiselect("Select or type missing toes: ", vals)     # list 
    
    #--- 3. Search
    #----- testcases
    #toes_choice = ['LF1', 'LF2', 'LF3', 'LF4', 'LF5']
    
    newdf = df.loc[df['Toes'].apply(lambda x: len(set(x) - set(toes_choice)) == 0)]
    	      
    newdf['toes_len'] = newdf.Toes.apply(len)
    newdf = newdf.sort_values(by='toes_len', ascending=False).drop(columns='toes_len')
    #-- optional: remove all rows with *intact* toes
    newdf = newdf[newdf['Toes'].map(len) != 0]
    
    # first 5 rows weighted, the remaining part of the df ordered by descending - requested by team
    newdfa = newdf.iloc[:5]
    newdfb = newdf.iloc[5:]            
    newdfb = newdfb.sort_values(by='ID', ascending=False)    # order by ID descending
    # merge /concat
    frames = [newdfa, newdfb]
    res = pd.concat(frames)
    
    # get all with missing toes -->  df.Toes.apply(lambda x: len(x)!=0) 
    # or df['Toes'].map(len)!=0
    
    st.info("The first 5 results are weighted, the remaining results are ordered by descending skink ID number.")
    st.write(" ## Search Results: ##")   
    st.table(res.style.set_properties(**{'background-color': '#cfdaaa'}, subset=['ID']))




