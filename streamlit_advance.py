#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:50:03 2020

@author: parasn
"""


import streamlit as st
import pandas as pd
import numpy as np
import time

dataframe=pd.DataFrame(np.random.randn(10, 20),columns=('col %d' % i for i in range(20)))
st.table(dataframe)


st.text("This will appear first")

my_slot1=st.empty()

# Appends an empty slot to the app. We'll use this later.

my_slot2=st.empty()

# Appends an empty slot to the app. We'll use this later.

st.text("This will appear last")

my_slot1.text("text in slot 1")

my_slot2.text("text in slot 2")

st.write("Animate Elements")

progress_bar=st.progress(0)
status_text=st.empty()
chart=st.line_chart(np.random.randn(10,2))

for i in range(100):
    #update progress bar
    progress_bar.progress(i+1)
    new_rows=np.random.randn(10,2)
    status_text.text('laytest number is %s' %new_rows[-1,1])
    chart.add_rows(new_rows)
    time.sleep(0.1)
    
status_text.text("done")
st.balloons()


st.write("Append data to a table or chart")
data=np.random.randn(10,2)


chart=st.line_chart(data)

time.sleep(1)

data2=np.random.randn(10,2)

chart.add_rows(data2)