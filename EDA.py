import streamlit as st
from visualize import time_series
def show(df):
    st.header('EDA')
    st.subheader('Yield')
    #st.dataframe(df.info())
    st.dataframe(df.head(5))
    st.subheader('Statistics')
    st.write(df['Yield'].describe())
    st.subheader('Yield vs Year')
    fig=time_series(df)
    st.pyplot(fig)