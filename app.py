import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from collections import Counter

st.set_page_config(page_title="News Sentiment Dashboard")

if 'data' not in st.session_state:
    response = requests.get("http://localhost:8000/")
    if response.status_code == 200:
        st.session_state.data = response.json()
    else:
        st.error("Failed to fetch data!")
        st.stop()

df = pd.DataFrame(st.session_state.data)
st.title("Real-time News Headlines")
st.dataframe(df[['headline']], use_container_width=True)