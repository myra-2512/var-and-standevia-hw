import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df= pd.read_csv('Bestsellers with categories.csv')
print(df.head())

print(df.isnull().any())

print(df['User Rating'].var())
print(df['User Rating'].std())

print(df['Price'].var())
print(df['Price'].std())

plt.hist(df['User Rating'], bins=10, edgecolor='black',color='seagreen')
plt.title('Distribution of User Ratings')
plt.xlabel('User Rating')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['Price'], bins=10, edgecolor='black',color='salmon')
plt.title('Distribution of Prices') 
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()