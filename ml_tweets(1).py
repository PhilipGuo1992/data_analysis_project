import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


def class_number(class_string):
    if class_string == 'positive':
        return -1
    if class_string == 'negative':
        return 1


df = pd.read_csv('train.csv')
df['class'] = df['Sentiment'].map(class_number)

X = df['SentimentText']
Y = df['class']
x_train, y_train = X, Y
df3 = pd.read_csv('stock_tweets.csv')
x_test = df3['SentimentText']

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('feat', SelectKBest(chi2, k=30)),
    ('clf', LogisticRegression())
    ])
pipeline.fit(x_train, y_train)
pipe_result = pipeline.predict(x_test)
df2 = pd.DataFrame
df2 = df3[['date', 'retweets', 'favorites', 'SentimentText']].copy()
df2.loc[:, 'score'] = pipe_result
df2.to_csv('stock_tweets.csv')










