import pandas as pd
import numpy as np
import streamlit as st

#@st.cache_data
def load_data():
    df=pd.read_excel("Arusha_AI.xlsx")
    #df=pd.DataFrame(data)
    Year=df['Year']
    Month=df["Month"]
    Yield=df["Yield"]
    rain=df["PREC"]
    tmx=df["TMX"]
    tmx=df["TMN"]
    return df

def features(df):
    X=df.iloc[:,2:6].values
    y=df.iloc[:,1]
    return X,y