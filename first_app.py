#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:30:44 2020

@author: parasn
"""

import streamlit as st
import pandas as pd
import numpy as np
st.title("first app")

st.write("Here is first attempt to create data frame")

st.write(pd.DataFrame({'firts_columm':[1,2,3,4],
                       'second_column':[10,20,30,40]}))

"""
Here is first application with magic commands
"""

df=pd.DataFrame({'first_column':[1,2,3,4],
                       'second_column':[10,20,30,40]})

df


# draw a line chart
st.write("Draw a line chart")
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])

chart_data
st.line_chart(chart_data)

st.write("Plot a map")
map_data=pd.DataFrame(np.random.randn(1000,2)/[50,50]+[37.76,-122.4],
                      columns=['lat','lon'])

map_data

st.map(map_data)


st.write("Adding widgets")
if st.checkbox("Show Dataframe"):
    chart_data=pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])

    chart_data
    st.line_chart(chart_data)
    

st.write("st.selectbox()")
option=st.selectbox("Which number do you want to select ?",df['first_column'])
'you selected',option


st.write("st.sidebar.[element_name]().")
option1=st.sidebar.selectbox("Which number do you want to select ?",chart_data['A'])
'you selected',option1

st.write("Show Progress")

import time
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
