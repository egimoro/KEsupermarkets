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

# %%

# Group unitPrice by intervals of 100 for prices [0,5000),
#  and sum no_of_items and total

price_start = 0

price_end = 5000

price_interval = 100

# Creating the buckets to collect the data accordingly

buckets = np.arange(price_start, price_end, price_interval) 

# Select the data and sum

revenue_per_price = df.groupby(pd.cut(df.unitPrice,
                               buckets)).total.sum()

revenue_per_price.head()

# %%

revenue_per_price.plot()

plt.xlabel('Unit Price (in intervals of '+str(price_interval)+')')

plt.ylabel('Total')

plt.show()

# %%

# Count how many items are food

food_item = df[df.food == 'yes']

len(food_item)

# %%

# Set the 'type_market' column as the index of the dataframe

df.set_index('type_market', inplace=True)

# Print only the beverage column

df.beverage

# %%

# Print the columns 'mall' and 'bevarage'

df[['mall', 'beverage']]

# %%

# Name of all columns

df.columns

# %%

# Select the 'Supermarket', 'Change', 'Type' columns from small and chain

df.loc[['small', 'chain'], ['supermarket', 'change', 'type']]

# %%

# Select the rows 3 to 7 and the columns 3 to 6

df.iloc[2:7, 2:6]

# %%

# Select every row after the fourth and all columns

df.iloc[4:, :]

# %%

# Select every row up to the 4th row and all columns

df.iloc[:4, :]

# %%

# Select the 3rd column up to the 7th column

df.iloc[:, 2:7]

# %%

# Select rows where df.change is greater than 1500

df[df['change'] > 1500]

# %%

# Select rows where df.change is greater than 1500 or less than 150

df[(df['change'] > 1500) | (df['change'] < 150)]

# %%

# Select all the location not 'saika'

df[df['location'] != 'saika']

# %%

# Reset index

df.reset_index()

# %%

# Set column 'time_type' as index

try:
    df.set_index('time_type', inplace=True)
except Exception:
    print('Something wrong')

df

# %%

# Select rows morning and evening

df.loc[['morning', 'evening']]

# %%

# Select the third cell in the row afternoon

df.loc[['afternoon']].iloc[:, 2]

# %%

# Select the third cell down in the column named variation

df.loc[:, ['variation']].iloc[2]

# %%

# Select rows afternoon and morning from the columns total to snack

s = df.loc[['afternoon', 'morning']].iloc[:, 3:9]

s

# %%

# Group selected dataset by column snack

s.groupby('snack').sum()

# %%

# Group by the snack the mean of columns with numeric values

sg = s.groupby('snack').mean()

sg


# %%
