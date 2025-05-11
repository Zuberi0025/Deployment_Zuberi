import streamlit as st
from data import load_data

df=load_data()
st.title('Yield Prediction')
st.sidebar.title('Selection')
page=st.siderbar.radio("Enter",['EDA'])
EDA.show(df)