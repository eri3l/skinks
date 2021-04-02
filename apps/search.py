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
    
    st.title("Skinks Search Tool")
    #--- 1. Load data
    def load_file(filename):
        
        df = pd.read_csv(filename, converters={'Trap': eval, 'Toes':eval})
        df['Sex'] = df['Sex'].astype(str)

        return df 
    
    df = load_file("source02.csv")
    
    #--- 2. Make button lists
    
    cols = df[['Toes', 'SVL', 'Trap']]
    cols_list = list(cols.columns.values)
    
    #------ st sidebar
    st.sidebar.title("Select search criteria")
    
    #------ 2.1. SVL
    
    svl_choice = st.sidebar.slider("SVL in mm", 0, 100, 50)  
    
    # NB: here add the condition for case where svl=69, it should search +/-5 range, so 65 to 100. 
    # remember that Projected_SVL is set in the makecsv.py file as any >=70 to be 100. 
    
    alpha = 5   # range of svl search
    adult = 100  # svl of adult skink in Projected_SVL, anything over 70
    svl_min = svl_choice - 5
    svl_max = svl_choice + 5
    if svl_max >= 70:
        svl_max = adult
    if svl_min >= 70:
        svl_min = adult
        
        
    #------ 2.2. Trap
      
    # FIXME: the horror! use the GPS coords instead
    # TODO: user-friendly names of vars pls
    
    pdk_R66 = ['R66', 'board', 'R67', 'M14', 'R68', 'R69', 'R70', 'M11', 'PR1']
    pdk_R71 = ['R71', 'PR2', 'R72', 'M9', 'P3', 'PR3', 'R73', 'M8', 'PR4', 'R74', 'M7', 'PR5', 'R75', 'PR6', 'R76', 'M5', 'PR7']
    pdk_R77 = ['R77', 'M4', 'PR8', 'PR78', 'M3', 'PR9', 'R79', 'M2', 'PR10', 'R80', 'PR11', 'R1', 'PR12']
    pdk_R02 = ['R2', 'PR13', 'R3', 'PR14', 'R4', 'PR15', 'P16', 'PR16', 'R6', 'PR17']
    pdk_w = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12', 'W13']
    pdk_R07 = ['R7', 'PR18', 'R08', 'P19', 'PR19', 'R9', 'PR20', 'R10', 'PR21', 'R11', 'P22', 'PR22', 'R12', 'PR23', 'R13']
    pdk_b = ['B1', 'B2', 'B3', 'B4']
    pdk_R14 = ['R14', 'P25', 'R15', 'P54', 'P53', 'PR53', 'P26', 'R16', 'PR55', 'R17', 'PR57', 'R18', 'PR59', 'P63', 'PR63', 'PR65', 'R22', 'PR67', 'PR71', 'R25', 'R26', 'R27', 'R28', 'PR77', 'R29', 'PR79', 'R30', 'P41', 'farm']
    pdk_P42 = ['P42', 'P84', 'R31', 'GM32', 'P90', 'R34', 'R35', 'R36', 'P98', 'R81', 'M41', 'R82', 'R83', 'R85', 'R86', 'R87', 'R88', 'M48', 'R89', 'R90', 'M50', 'R91', 'R92', 'M52']
    pdk_R93_removed = ['R93', 'M53', 'R94', 'M54', 'R95', 'R97', 'M57', 'R98', 'R99', 'R100', 'R101', 'M61', 'P135', 'R102', 'R103', 'R104', 'P138', 'R105', 'R106', 'R108', 'R121', 'R126']
    
    pdk_R14_1st_half = ['R14', 'P25', 'R15', 'P54', 'P53', 'PR53', 'P26', 'R16', 'PR55', 'R17', 'PR57', 'R18', 'PR59', 'P63']
    pdk_R14_2nd_half = ['PR65', 'R22', 'PR67', 'PR71', 'R25', 'R26', 'R27', 'R28', 'PR77', 'R29', 'PR79', 'R30', 'P41', 'farm']
    pdk_P42_1st_half = ['P42', 'P84', 'R31', 'GM32', 'P90', 'R34', 'R35', 'R36', 'P98', 'R81', 'M41', 'R82']
    pdk_P42_2nd_half = ['R85', 'R86', 'R87', 'R88', 'M48', 'R89', 'R90', 'M50', 'R91', 'R92', 'M52']
    
    trap_options = ['pdk_R66', 'pdk_R71', 'pdk_R77', 'pdk_R02', 'pdk_R14', 'pdk_P42', 'pdk_R93_removed',
                    'pdk_w', 'pdk_b',
                    'pdk_R14_1st_half', 'pdk_R14_2nd_half', 'pdk_P42_1st_half', 'pdk_P42_2nd_half']
    
    dicta = {}
    
    #------- a. create dictionary keys from variables
    for i in ['pdk_R66', 'pdk_R71', 'pdk_R77', 'pdk_R02', 'pdk_R14', 'pdk_P42', 'pdk_R93_removed',
                    'pdk_w', 'pdk_b',
                    'pdk_R14_1st_half', 'pdk_R14_2nd_half', 'pdk_P42_1st_half', 'pdk_P42_2nd_half']:
        dicta[i] = eval(i)
        
    
    t_choice = st.sidebar.multiselect("Select a trap group/list: ", trap_options)  # ret str
    
    # # debug msg
    # st.write(svl_choice, t_choice)
    
    #------ b. put the traplist choice in a dict, in order to map the name str or k to the value
    
    t_val = [None] * len(t_choice)
    dictb = dict(zip(t_choice, t_val))
    
    for k, v in dictb.items():
            if k in dicta: 
               dictb[k] = dicta[k]
    
    # debug msg
    #   st.write(dictb)
    #st.write("the trap names are: ", dictb.keys(), " and the traps inside them: ", dictb.values())
    #st.write("dict items: ", dictb.items())
    #------ c. search prep
    
    trap_choice = []
    for k,v in dictb.items():
        trap_choice.append(v)
    
    #------ 2.3. Toes
    toes_vals = ['intact', 'toes missing']
    t_choice = st.sidebar.selectbox("Select toes: ", toes_vals)      # str
    toes_choice = []
    missing_vals = np.unique([*itertools.chain.from_iterable(df.Toes)]) # get all unique toes from df.Toes
    
    if t_choice == 'toes missing':
        # add some default here because initially toes_choice is a []
        #toes_choice = missing_vals
        toes_choice = st.sidebar.multiselect("Select or type missing toes: ", missing_vals)     # list ['LF1']
        #st.write("Inside: ", type(toes_choice))
    elif t_choice == 'intact':
        toes_choice = []
        
    # debug
    # st.write("Type of toes: ", type(toes_choice))
    # st.write(toes_choice)
    
    #--- 3. Search
    #----- testcases
    # trap_choice = ['R66', 'board', 'R67', 'M14', 'R68', 'R69', 'R70', 'M11', 'PR1']  # list
    # toes_choice = ['LF1']   # list
    # toes_ch = []        # list  for intact
    
    
    newdf = df.loc[ df.Trap.apply(lambda x: bool(set(x).intersection( list(chain.from_iterable(trap_choice)) ))) &
                   ( df['Toes'].apply(lambda x: len(set(x) - set(toes_choice)) == 0)) &
                   ((df['projected_SVL'] >= svl_min) & (df['projected_SVL'] <= svl_max) )       # TODO: try between()
                   ]
    if t_choice == 'toes missing':
        newdf['toes_len'] = newdf.Toes.apply(len)
        newdf = newdf.sort_values(by='toes_len', ascending=False).drop(columns='toes_len')
        #-- optional: remove all rows with *intact* toes
        newdf = newdf[newdf['Toes'].map(len) != 0]
    
    # get all with missing toes -->  df.Toes.apply(lambda x: len(x)!=0) 
    # or df['Toes'].map(len)!=0
    
    
    st.write("SEARCH RESULTS")    
    st.table(newdf)
    
    #<sub><sup>combining the two tags</sup></sub>
    st.markdown('Your selected criteria are: `SVL`: {},  \n  `Trap`: {},  \n  `Toes`: {}'.format(svl_choice, trap_choice, toes_choice),
                unsafe_allow_html=True)
