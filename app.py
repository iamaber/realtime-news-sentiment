import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from collections import Counter

st.set_page_config(page_title="News Sentiment Dashboard")

if "data" not in st.session_state:
    response = requests.get("http://localhost:8000/")
    if response.status_code == 200:
        st.session_state.data = response.json()
    else:
        st.error("Failed to fetch data!")
        st.stop()

df = pd.DataFrame(st.session_state.data)
st.title("Real-time News Headlines")
st.dataframe(df[["headline"]], use_container_width=True)

# Analyze Sentiment
if st.button("Run Sentiment Analysis"):
    sentiment_counts = Counter(
        [item["sentiment"]["label"].upper() for item in st.session_state.data]
    )

    labels = list(sentiment_counts.keys())
    values = list(sentiment_counts.values())
    colors = {
        "POSITIVE": "green",
        "NEGATIVE": "red",
        "NEUTRAL": "gray",
        "UNKNOWN": "lightgray",
    }

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                marker=dict(colors=[colors.get(label, "blue") for label in labels]),
            )
        ]
    )
    fig.update_layout(title="Sentiment Distribution")
    st.plotly_chart(fig)

    # Detailed Sentiment Table
    st.subheader("Sentiment Details")
    sentiment_labels = []
    sentiment_scores = []
    color_labels = []

    for item in st.session_state.data:
        sentiment = item["sentiment"]
        label = sentiment.get("label", "UNKNOWN").upper()
        score = sentiment.get("score", 0.0)

        sentiment_labels.append(f"{label}")
        sentiment_scores.append(f"{score:.2f}")

    df["Sentiment"] = sentiment_labels
    df["Score"] = sentiment_scores

    st.dataframe(df[["headline", "Sentiment", "Score"]])
