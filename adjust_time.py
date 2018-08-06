import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def class_number(class_string):
    if class_string < 0:
        return -1
    if class_string > 0:
        return 1
    else:
        return 0

df = pd.read_csv('stock_tweets.csv')
df['date'] = pd.to_datetime(df.date)
df['date'] = df.date + timedelta(days=1)
df.to_csv('stock_tweets.csv')
