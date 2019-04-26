import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('bollywood_kaggle.csv')

# drop unneeded columns
data = data.drop('Genre', axis=1)
data = data.drop('Title', axis=1)

# create new column with the directors and cast combined, properly formatted
data['Director'] = data['Director'].str.replace(' ',',')
data['People'] = data['Director'] + "," + data["Cast"]
data['People'] = data['People'].str.replace('(','')
data['People'] = data['People'].str.replace(')','')

# drop unneeded columns
data = data.drop('Cast', axis=1)
data = data.drop('Director', axis=1)

# split People column by comma
data = data.join(data.People.str.split(',', expand=True))
data = data.drop('People', axis=1)

# read in descending order
data = data.iloc[::-1]


print(data.head())
