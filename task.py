import pandas as pd
import numpy as np
import re

from textblob import TextBlob

class TweetAnalyzer():

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
           return -1
	
    def tweets_to_data_frame(self):
        arr_of_tweets = []
        tweet_analyzer = TweetAnalyzer()
		
        col_list = ["text"]
        df = pd.read_csv("tweets.csv", usecols=col_list)
		
        df['text'] = df['text'].replace(np.nan, '')
		
        for tweet in df['text']:
            text = self.clean_tweet(tweet)
            arr_of_tweets.append(text)
			
        df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in arr_of_tweets])
		
        #store all 100 tweets in .csv file
        df.to_csv('tweets_analysis.csv')
        #print the top 10 tweets
        print(df.head(10))
        pass

if __name__ == '__main__':
    obj1 = TweetAnalyzer()
    obj1.tweets_to_data_frame()

