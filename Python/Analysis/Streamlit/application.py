import streamlit as st
import pandas as pd
import plotly.express as px
from application_function import pca_maker 

st.set_page_config(layout="wide")

scatter_column, settings_column = st.columns([4, 1])

scatter_column.title("Multi Dimensional Analysis")

settings_column.title("Settings")

uploaded_file = settings_column.file_uploader("Choose File")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    pca_data, cat_cols, pca_cols = pca_maker(df) 
    
else:
    scatter_column.header("Please Choose a File")
    