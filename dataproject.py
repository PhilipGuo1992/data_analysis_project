import csv
import pandas as pd
import numpy as np
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

new_words = {
    'up': 4,
    'buy': 4,
    'increase': 4,
    'sell': -4,
    'lost': -4,
    'fall': -4,
    'plunge': -4,
    'down': -4
}

sentences = [
            "Twitter down 27% in past 2 trading days, worst two-day decline since it went public in Nov 2013. $TWTR ",
            "I love seeing the stocks of lefty Censors like $FB and $TWTR getting destroyed",
            "$TWTR Twitter ...Don't do it, man. Think about your future. Think about your family! ",
            "Really looking forward to people using #Twitter to talk shit about $TWTR",
            "I want to buy it $FB",
             "$FB lost $145B market cap in 90 minutes",
             # down is treated as neutral; so, I add 'down' to dictionary
             "stock price goes down",
            "This 20% plunge in Facebook",
            "Markets need a bad week to scare the Fed. Trump wants to scare the Fed. Tesla also needs the Fed not to raise interest rates. Other tech stocks want the bleeding to stop before the pain doubles (or more). What an interesting week! $ DJIA $ NASDAQ $ TSLA $ TWTR $ FB $ NFLX",
            "On the bright side, Zuckerberg has lost $22 billion or so since the stock market closed.",
            "Chrome and Safari will offer similar features, presumably. Not positive for Facebook's ad revenue or stock price. $ FB https://twitter.com/waxpancake/status/978708653472587776 â€¦"
             ]

analyzer = SentimentIntensityAnalyzer()

# add new words to your dictionary
analyzer.lexicon.update(new_words)

for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
    print (vs["compound"])

# # manipulate csv
# # clean it first
df = pd.read_csv('twtr_stock.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
# # drop date not correct type
df = df.dropna(subset=['date'])
#
# # convert datetime to date
df['just_date'] = df['date'].dt.date
#
# # calculate sentiment score
score = []
for row in df['text']:
    vs = analyzer.polarity_scores(row)
    compound_score = vs["compound"]
    score.append(compound_score)

df['sentiment_score'] = score
# # print (df['sentiment_score'])
#
# # group column by date: calculate the average sentiment score for each day.
df2 = pd.DataFrame
#
# # df2['score'] = df['sentiment_score'] * df['retweets'] + df['sentiment_score'] + df['sentiment_score'] * df['favorites'] * 0.1
df3 = df['sentiment_score'].astype(float) * df['retweets'].astype(float) + df['sentiment_score'].astype(float) + df['sentiment_score'].astype(float) * df['favorites'].astype(float) * 0.1
array_ = np.array(df3)
df.loc[:, 'total_score'] = array_
#

# df2 = df.groupby('just_date')['sentiment_score'].apply(lambda x: np.average(x))
# print (df)
# save results to csv
with open("twtr_output.csv", "wb") as outputfile:
    df.to_csv(outputfile)















