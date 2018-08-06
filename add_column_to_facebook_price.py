import pandas as pd
import numpy as np


def class_number(class_string):
    if class_string < 0:
        return -1
    if class_string > 0:
        return 1

df = pd.read_csv('facebook.csv')
df2 = pd.DataFrame
df2 = df['Close']-df['Open']
df2 = np.array(df2)
df.loc[:, 'state'] = df2
df['state'] = df['state'].map(class_number)
df.to_csv('facebook_stock_price.csv')

