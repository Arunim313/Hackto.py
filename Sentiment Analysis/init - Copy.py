import os
from transformers import pipeline
import tweepy as tp
import configparser as cp
import numpy as np
import csv
import pandas as pd
import streamlit as st

config = cp.ConfigParser()
config.read('config.ini')

api_key = ""
api_secret = ""

access_token = ""
access_token_secret = ""

auth = tp.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth)

sentiment_analysis = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")