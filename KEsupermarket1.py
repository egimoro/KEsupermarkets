# %%

import pandas as pd
import numpy as np

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
