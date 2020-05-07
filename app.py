import streamlit as st
import pandas as pd
import numpy as np
import home

st.title('Uber pickups in NYC')

# Add a selectbox to the sidebar:
page = st.sidebar.selectbox(
    'Select a page to work?',
    ('Home', 'analysis 1', 'analysis 2')
)

if page == 'Home':
    home.get_home_page()
elif page == 'analysis 1':
    st.write('nothing here')
elif page == 'analysis 2':
    st.write("one day")
else:
    st.write("no page selected")    

