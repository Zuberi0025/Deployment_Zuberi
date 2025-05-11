import pandas as pd
import numpy as np
import streamlit as st

#@st.cache_data
def load_data():
    data=pd.read_excel("Arusha_AI.xlsx")
    Year=data['Year']
    Month=data["Month"]
    Yield=data["Yield"]
    rain=data["PREC"]
    tmx=data["TMX"]
    tmx=data["TMN"]
    return load_data

def features(data):
    X=data.iloc[:,2:6].values
    y=data.iloc[:,1]
    return X,y