import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('SaratogaHouses.csv')

X = dataset['rooms']
plt.hist(X)
plt.show()
