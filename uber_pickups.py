#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:33:33 2020

@author: parasn
"""

#create data explorer app
#Step 1.The first step is to create a new Python script. 
#Let’s call it uber_pickups.py.
#Step 2. Add libraries
#Step 3. Put an application title 

import streamlit as st
import pandas as pd
import numpy as np


st.title("uber pickups in NYC")


DATA_COLUMN ='date/time'
DATA_URL=('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data=pd.read_csv(DATA_URL,nrows=nrows)
    lowercase=lambda x:str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    data[DATA_COLUMN]=pd.to_datetime(data[DATA_COLUMN])
    return data


    
data_load_state=st.text('Loading data')
data=load_data(10000)
data_load_state.text('Loading data...done!!')
data_load_state.text("Done! (using st.cache)")


#inspect the row data
st.subheader("Raw data")
if st.checkbox("Show Raw Data"):
    st.write(data)
    
st.subheader("Number oof pickups by hour")
hist_values=np.histogram(data[DATA_COLUMN].dt.hour,bins=24,range=(0,24))[0]
st.bar_chart(hist_values)


hour_to_filter=st.slider('hour',0,23,17)
filterred_data=data[data[DATA_COLUMN].dt.hour==hour_to_filter]
st.subheader("Map of al pickups at %s:00" % hour_to_filter)
st.map(filterred_data)
