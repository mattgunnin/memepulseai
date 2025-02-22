from transformers import pipeline
import tweepy

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")

    def analyze(self, text):
        result = self.sentiment_pipeline(text)[0]
        return {"label": result["label"], "score": result["score"]}

def fetch_x_posts(api_key, api_secret, access_token, access_secret, query, max_tweets=100):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(max_tweets)
    return [tweet.text for tweet in tweets]