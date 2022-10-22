from init import *
import streamlit as st

def SentimentAnalysis(sq):
    tweets = tp.Cursor(api.search_tweets,
              q = sq+'-filter:retweets',
              lang = "en",
              tweet_mode = "extended").items(500)
    data = []
    for tweet in tweets:
        try:
            content = tweet.full_text
            sentiment = sentiment_analysis(content)
            data.append([content, sentiment[0]['label']])
        except:
            pass
    columns = ['Tweet', 'Sentiment']
    df = pd.DataFrame(data, columns=columns)
    f = df.to_csv().encode('utf-8')
    return f