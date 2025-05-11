import streamlit as st
import EDA
from data import load_data
df=load_data()
st.title('Yield Prediction')
st.sidebar.title('Selection')
page=st.sidebar.radio("Enter",['EDA'])
EDA.show(df)