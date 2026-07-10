import matplotlib.pyplot as plt
import pandas as pd
# https://www.kaggle.com/code/arbazkhan971/indian-premier-league-analysis-2008-2025/input
df = pd.read_csv('appl_1980_2014.csv')
print(df.head())
# Line Graph
X = pd.to_datetime(df['Date'])
y = df['Adj Close']

# Line Plot
plt.plot(X,y)
plt.xlabel("DATE")
plt.ylabel("ADJ CLOSE")
plt.title("APPLE STOCKS DATE VS ADJ CLOSE")
plt.show()
