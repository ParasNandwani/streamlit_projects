#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:22:51 2020

@author: parasn
"""

import streamlit as st
import pandas as pd
import numpy as np
import time



st.write("Exmple 1 Basic Usage without cache")


def expensive_computation(a,b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)
    return a*b;


a=2
b=21
res= expensive_computation(a,b)

st.write("Result :",res)


st.write("Exmple 1 Basic Usage with cache")

@st.cache(suppress_st_warning=True)
def expensive_computation(a,b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)
    return a*b+1;


a=2
b=21
res= expensive_computation(a,b)

st.write("Result :",res)



st.write("Example 2. when the function arguments change")

a=2
b=210
res=expensive_computation(a,b)

st.write("Result :",res)

st.write("Example 3 when the function body chanmges")



a=2
b=210

res=expensive_computation(a,b)

st.write("Result :",res)
