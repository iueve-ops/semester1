import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BTC_data.csv')

close =df['close'].values
df['time'] = pd.to_datetime(df['time'])
time = df['time'].values

plt.plot(time,close, )
plt.xticks(ticks=df['time'][::200], labels=df['time'].dt.strftime('%d-%m-%y')[::200], rotation=45)

plt.show()