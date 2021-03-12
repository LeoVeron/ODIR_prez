import streamlit as st
st.set_page_config(layout="wide", page_title='LAS Explorer v.0.1')
import pandas as pd

# Local Imports
import home
import model
import data


# Sidebar Navigation
st.sidebar.title('# ODIR Project')
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:', 
    ['Home', 'Data Information', 'Model'])

if options == 'Home':
    home.home()
elif options == 'Data Information':
    data.data()
elif options == 'Model':
    model.model()