* task.py contains the code to do analysis of the tweets by reading it from tweets.csv file and store the analysed data into 
  tweets_analysis.csv file as well as printing first 10 records of analysed data on console.

* The tweets.csv is generated using an GetOldTweets-python tool which is essentially a tool that queries twitter search engines
  via the browser using python libraries such as pyquery, urllib, requests, and Lxml, below is the link for additional infomation about tool:-
  https://medium.com/analytics-vidhya/twitter-data-mining-mining-twitter-data-without-api-keys-a2a2bd3f11c

* task.py is written to show whether the tweets indicates negative, positive or neutral sentiments by analysing the use of racial slurs and obscene language in each tweet

* I have used GetOldTweets python tool to fetch the tweets which contains the racial slur "nigger" and store 100 tweets into
  tweets.csv file, below is the command which i executed to fetch the tweets:-

  python GetOldTweets3.py --querysearch "nigger" --maxtweets 100 --output tweets.csv

* To analyze a tweet for understanding the opinion expressed by it, we quantify the sentiment with a positive or negative value called polarity, the overall sentiment is often inferred as positive, neutral or negative from the sign of the polarity score.

* In task.py, polariy of tweet greater then 0 means positive sentiment, less then 0 means negative sentiment and equal to 0 means neutral sentiment.

* To get an idea of how the analysed data looks like, please go through output_in_csv.png and output_on_console.png files
