import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import numpy as np

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "01 annual-number-of-deaths-by-cause.csv")

st.title("Dashboard - Annual-number-of-deaths")


df = pd.read_csv(DATA_PATH)
st.dataframe(df)


country = st.selectbox("Select the country:", df['Entity'].unique())
col=st.selectbox("select way of deat",df.columns)

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Entity'] == country ], x='Year',y=col)
col1.plotly_chart(fig_1,use_container_width=True)
fig_2 = px.box(df[df['Entity'] == country], x='Year',y=col)
col2.plotly_chart(fig_2,use_container_width=True)

