import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('bollywood_kaggle.csv')
data = data.drop('Genre', axis=1)
data = data.drop('Title', axis=1)
cast = data.Cast.str.split(',', expand=True)
data = data.iloc[::-1]
data = data.drop('Cast', axis=1)
print(data.head())


ax = data[['Year','Director']].plot(kind='bar', title ="Year v Director", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Director", fontsize=12)
plt.show()
cast = cast.iloc[::-1]
print(cast.head())