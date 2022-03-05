import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="HR Dashboard", page_icon=":bar_chart:", layout="wide")

df = pd.read_csv('data/data.csv')


# SIDEBAR

st.sidebar.header("Filter here:")
gender = st.sidebar.multiselect(
    "Select gender:",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

st.sidebar.header("Filter here:")
ssc_b = st.sidebar.multiselect(
    "Select ssc_b:",
    options=df["ssc_b"].unique(),
    default=df["ssc_b"].unique()
)

df_selection = df.query(
    "gender == @gender & ssc_b == @ssc_b"
)

st.dataframe(df_selection)
