import streamlit as st

x = st.slider('select a valie')
st.write(x, 'squared is', x*x)