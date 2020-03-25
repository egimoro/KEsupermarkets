# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%

# Create a data frame of supermarkets

df = pd.DataFrame({'Supermarket': np.random.choice(['acacia', 'chandarana',
                  'tuskys', 'nakumatt', 'uchumi', 'eastmatt', 'ukwala',
                   'fairway', 'tumaini'], size=1000),
                   'Total paid': np.random.randint(70, 13000, size=1000),
                   'type': np.random.choice(['cash', 'card', 'mpesa'],
                                            size=1000)})

df                  

# %%

# Number of observations in the dataset

df.shape[0]

# %%

df.info()

# %%

# See first 10 entries

df.head(10)

# %%

# Number of columns in the dataset

df.shape[1]

# %%

# Print the name of all the columns

df.columns

# %%

# How is the dataset indexed?

df.index

# %%

# Read full dataset

Location = r'../KEsupermarkets/data.csv'

df = pd.read_csv(Location)

df

# %%

# Supermarkets where most items were bought

s = df.groupby('supermarket')

s = s.sum()

s = s.sort_values(['no_of_items'], ascending=False)

s.head(1)

# %%

# Locations where most items were bought

s = df.groupby('location')

s = s.sum()

s = s.sort_values(['no_of_items'], ascending=False)

s.head(1)

# %%

# Total items bought

total_items_bought = df.no_of_items.sum()

total_items_bought

# %%

# Find unit item price from total

price = (df['total']/df['no_of_items']).sum()

print('Total unit price item is: KSH ' + str(np.round(price, 2)))

# %%

# Group by location

Location = df.groupby('location').sum()

# Sort the value and get the second 10 locations

Location = Location.sort_values(by='no_of_items', ascending=False)[1:11]

# Create the plot

Location['no_of_items'].plot(kind='bar')

# Set the title and labels

plt.xlabel('Location')
plt.ylabel('Number of items')
plt.title('10 Locations with most items')

# Show the plot

plt.show()

# %%

# Find the unit price

unitPrice = df['total']/df['no_of_items']

unitPrice

# %%

# Add the new column

df['unitPrice'] = np.round(unitPrice, 2)

df
