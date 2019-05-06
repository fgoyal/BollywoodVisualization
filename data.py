import pandas as pd
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
data['People'] = data['People'].str.lower()

# drop unneeded columns
data = data.drop('Cast', axis=1)
data = data.drop('Director', axis=1)

# create new dataframe
unsplit = pd.DataFrame.copy(data, deep=True)
unsplit['People'] = unsplit['People'].str.replace(',',' ')

# gets list of names from user
input_names = input("Enter the actors you want visualized, separated by a comma.")
people_name = input_names.replace(', ', " and ")
input_names = input_names.lower().replace(', ', " ")
names = input_names.split()

filtered = unsplit

# loop through list and filter by names in list
for name in names:
    has_name = filtered['People'].str.contains(name)
    filtered = filtered[has_name]

# plt.figure(figsize=(15, 5))

# create year range
years = pd.Series(range(1920, 2018))

# get frequency counts and map to years
frequency = filtered['Year'].value_counts()
frequency = frequency.reindex(years, fill_value=0)

# create graph
title = people_name + ' through the years'
ax = frequency.plot(kind='line', x='Year', y='Appearances', title=title )
ax.set_xlabel("Year")
ax.set_ylabel("Appearances")
plt.show()
