# %%

import pandas as pd
import matplotlib.pyplot as plt


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

print(KEsupermarket)

# %%

df = pd.DataFrame(data=KEsupermarket, columns=['supermarkets', 'no_of_items',
                  'variation', 'total'])

print(df)

# %%

Sorted = df.sort_values(['supermarkets'], ascending=False)

Sorted.head(1)

# %%

print(df['no_of_items'].max())

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
