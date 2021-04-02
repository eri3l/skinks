import pandas as pd
import numpy as np
import streamlit as st
import itertools
import pickle5 as pickle	# for python 3.7 


st.title("Search by missing toes only")
#--- 1. Load data
def load_file(filename):
	#df = pd.read_csv(filename)

	# pd.eval() to read columns their corresponding dtype (only for str-list), instead of getting converted by by read_csv()
	df = pd.pickle.loads(filename)

	#df = pd.read_csv(filename, converters={'Trap': eval, 'Toes':eval})

	return df 

df = load_file("source02.pk")
