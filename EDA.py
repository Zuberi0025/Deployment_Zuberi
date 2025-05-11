import streamlit as st
from visualize import time_series
def show(data):
    st.header('EDA')
    st.subheader('Yield')
    st.dataframe(data.head(5))
    st.subheader('Statistics')
    st.write(data['Yield'].describe())
    
    st.subheader('Yield vs Year')
    fig=time_series(data)
    st.pyplot(time_series)