# %%

import pandas as pd
import matplotlib.pyplot as plt
from numpy import random


supermarkets = ['acacia', 'acacia', 'acacia', 'acacia', 'nakumatt', 'tuskys',
                'chandarana', 'nakumatt', 'nakumatt', 'nakumatt', 'nakumatt',
                'uchumui', 'naivas', 'naivas', 'naivas', 'naivas',
                'naivas', 'naivas', 'naivas', 'karrymart', 'karrymart']

no_of_items = [1, 2, 6, 8, 33, 44, 14, 6, 8, 9, 6, 5, 1,
               2, 3, 6, 7, 5, 8, 10, 23]

variation = [1, 1, 2, 2, 13, 6, 2, 1, 3, 1, 1, 4, 2, 3,
             1, 1, 3, 2, 1, 2, 1, 2, 2, 6]

total = [90, 70, 270, 137, 5611, 55, 7955, 780, 235, 13005, 431, 1000, 242,
         4926, 5439, 5439, 8110, 221, 584, 850, 90]

KEsupermarket = list(zip(supermarkets, no_of_items, variation, total))

KEsupermarket

# %%

df = pd.DataFrame(data=KEsupermarket, columns=['supermarkets', 'no_of_items',
                  'variation', 'total'])

df

# %%

Sorted = df.sort_values(['supermarkets'], ascending=False)

Sorted.head(1)

# %%

df['no_of_items'].max()

# %%

df['variation'].plot()

MaxValue = df['variation'].max()

MaxSupermarket = df['supermarkets'][df['variation'] == df['variation'
                    ].max()].values

Text = str(MaxValue) + " - " + MaxSupermarket

plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
             xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular supermarket")

df[df['supermarkets'] == df['supermarkets'].max()]


# %%

df.to_csv('KEsupermarkets.csv', index=False, header=False)

# %%

Location = '../KEsupermarkets/KEsupermarkets.csv'

df = pd.read_csv(Location)

df

# %%

df = pd.read_csv(Location, header=None)

df

# %%

df = pd.read_csv(Location, names=['supermarkets', 'no_of_items',
                                  'variation', 'total'])

df

# %%

random.seed(500)

random_supermarkets = [supermarkets[random.randint(low=0,
                       high=len(supermarkets))] for i in range(1000)]

random_supermarkets

# %%

random_supermarkets[:10]

# %%

total_price = [random.randint(low=0, high=1000) for i in range(1000)]

total_price

# %%

total_price[:10]

# %%

SuperMarketDataSet = list(zip(random_supermarkets, total_price))

SuperMarketDataSet[:10]

# %%

df = pd.DataFrame(data=SuperMarketDataSet, columns=['Supermarkets', 'Total'])

df[:10]


# %%

df.to_csv('KEsupermarkets.txt', index=False, header=False)

# %%

Location = r'../KEsupermarkets/KEsupermarkets.txt'

df = pd.read_csv(Location)

df.info()

# %%

df.head()

# %%

df = pd.read_csv(Location, header=None)

df.info()

# %%

df.tail()

# %%

df = pd.read_csv(Location, names=['Supermarkets', 'Total'])

df.head(5)

# %%

df = pd.read_csv(Location, header=None)

df.info()

# %%

df.tail()

# %%

df = pd.read_csv(Location, names=['Supermarkets', 'Total'])

df.head()

# %%

df['Supermarkets'].unique()

# %%

for x in df['Supermarkets'].unique():
    print(x)

# %%

print(df['Supermarkets'].describe())

# %%

supermarket = df.groupby('Supermarkets')

df = supermarket.sum()

df

# %%

Sorted = df.sort_values(['Total'], ascending=False)

Sorted.head(1)

# %%

df['Total'].max()

# %%

df['Total'].plot.bar()

print('The most popular supermarket')

df.sort_values(by='Total', ascending=False)


# %%
