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

# # split People column by comma
# data = data.join(data.People.str.split(',', expand=True))
# data = data.drop('People', axis=1)
#
# # read in descending order
# data = data.iloc[::-1]

# search for amitabh bachchan
has_amitabh = unsplit['People'].str.contains('kajol')
has_bachchan = unsplit['People'].str.contains('')
has_amitabh1 = unsplit['People'].str.contains('shah')
has_bachchan2 = unsplit['People'].str.contains('rukh')
has_bachchan3 = unsplit['People'].str.contains('khan')
filtered = unsplit[has_amitabh & has_bachchan & has_amitabh1 & has_bachchan2 & has_bachchan3]

# create year range
years = pd.Series(range(1920,2018))

# get frequency counts and map to years
frequency = filtered['Year'].value_counts()
frequency = frequency.reindex(years, fill_value=0)

# create graph
# frequency.sort_index(axis=0, level=None, ascending=True, inplace=True, sort_remaining=True)
plt.figure(figsize=(15, 5))
ax = frequency.plot(kind='line', x='Year', y='Appearances')
ax.set_xlabel("Year")
ax.set_ylabel("Actor Appearances")
