import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import numpy as np

from bokeh.plotting import figure

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "GOI.csv")

st.title("Dashboard - literacyrate of india")


df = pd.read_csv(DATA_PATH)
st.dataframe(df)



chart_data = pd.DataFrame(df)
col1, col2 = st.columns(2)
with col1:
    st.bar_chart(chart_data,x="Country/ States/ Union Territories Name", y="Literacy Rate (Persons) - Total - 2011")
with col2:
    st.bar_chart(chart_data,x="Country/ States/ Union Territories Name", y="Literacy Rate (Persons) - Total - 2001")
    
state = st.selectbox("Select the state:", df['Country/ States/ Union Territories Name'].unique())
