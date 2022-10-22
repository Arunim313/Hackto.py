import SenAnal
import streamlit as st

st.image('twitter.png', width=80)
st.title("Twitter Sentiment Analysis")
search_query = st.text_input('Twitter Keywords')
if len(search_query) != 0:
    st.download_button(label='Download', data=SenAnal.SentimentAnalysis(search_query), file_name='data.csv')