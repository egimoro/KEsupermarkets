# %%

# Import libraries

import pandas as pd 
# Library for plotting
import matplotlib.pyplot as plt
from numpy import random
import numpy.random as np

# Create lists of supermarkets, number of items, and total paid

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

# Create a data set with a zip function

KEsupermarket = list(zip(supermarkets, no_of_items, variation, total))

# Run the script

KEsupermarket

# %%

# Create another object called datadrame

df = pd.DataFrame(data=KEsupermarket, columns=['supermarkets', 'no_of_items',
                  'variation', 'total'])

df

# %%

# Analysis of the dataframe

Sorted = df.sort_values(['supermarkets'], ascending=False)

Sorted.head(1)

# %%

df['no_of_items'].max()

# %%

# Plot the dataframe

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

# Export the dataframe into a csv format

df.to_csv('KEsupermarkets.csv', index=False, header=False)

# %%

# Create the variable location to read where the data is stored

Location = '../KEsupermarkets/KEsupermarkets.csv'

df = pd.read_csv(Location)

df

# %%

# Correct the header because it puts the first values of the data frame as a header

df = pd.read_csv(Location, header=None)

df

# %%

# Create a new header with column names

df = pd.read_csv(Location, names=['supermarkets', 'no_of_items',
                                  'variation', 'total'])

df

# %%

# Generate a random sample with
# a random integer between 0 and the length of the list "supermarkets"
# Loop until i is equal to 1000 supermarkets

random.seed(500)

random_supermarkets = [supermarkets[random.randint(low=0,
                       high=len(supermarkets))] for i in range(1000)]


random_supermarkets

# %%

# Print the first 10 records of random supermarkets

random_supermarkets[:10]

# %%

# Apply the same operations with the total price as the previous one

total_price = [random.randint(low=0, high=1000) for i in range(1000)]

total_price

# %%

total_price[:10]

# %%

# Create a supermarket data set

SuperMarketDataSet = list(zip(random_supermarkets, total_price))

# Print first 10 records of the data set

SuperMarketDataSet[:10]

# %%

# Create the supermarket dataframe and print first 10 records

df = pd.DataFrame(data=SuperMarketDataSet, columns=['Supermarkets', 'Total'])

df[:10]


# %%

# Export the file in csv format but in a text file

df.to_csv('KEsupermarkets.txt', index=False, header=False)

# %%

# Location of file

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

# Print unique values

df['Supermarkets'].unique()

# %%

for x in df['Supermarkets'].unique():
    print(x)

# %%

print(df['Supermarkets'].describe())

# %%

# Create a groupby object

supermarket = df.groupby('Supermarkets')

# Apply the sum function to the groupby object

df = supermarket.sum()

df

# %%

# Analyse data by sorting values

Sorted = df.sort_values(['Total'], ascending=False)

Sorted.head(1)

# %%

df['Total'].max()

# %%

# Create bar graph

df['Total'].plot.bar()

print('The most popular supermarket')

df.sort_values(by='Total', ascending=False)


# %%

# Set seed

np.seed(111)

# Function to generate test data


def CreateDataSet(Number=1):

    Output = []

    for i in range(Number):
        
        rng = pd.date_range(start='1/1/2016', end='31/12/2019', freq='W-MON')

        data = np.randint(low=25, high=1000, size=len(rng))

        status = [1, 2, 3]

        random_status = [status[np.randint(low=0, 
                         high=len(status))] for i in range(len(rng))]

        location = ['SA', 'ya', 'KI', 'DO', 'UM', 'EL']

        random_location = [location[np.randint(low=0, 
                           high=len(location))] for i in range(len(rng))]

        Output.extend(zip(random_location, random_status, data, rng))

    return Output


dataset = CreateDataSet(4)

df = pd.DataFrame(data=dataset, columns=['Location', 'Status', 
                                         'CustomerCount', 'StatusDate'])

df.info()

# %%

df.head()

# %%

# Save results to excel

df.to_excel('Lesson3.xlsx', index=False)
print('Done')

# %%

df['Location'].unique()

# %%

# Clean Location Column, convert to upper case

df['Location'] = df.Location.apply(lambda x: x.upper())

df['Location'].unique()

# %%

# Only grab where Status == 1

mask = df['Status'] == 1

df = df[mask]

# Convert SA to SK

mask = df.Location == 'SA'

df['Location'][mask] = 'SK'

df['Location'].unique()

# %%

# Plot customer data

df['CustomerCount'].plot(figsize=(15, 5))

# %%
