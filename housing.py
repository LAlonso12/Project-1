import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reads the housing data from the CSV file into pandas DataFrame
housing_data = pd.read_csv('housing_data.csv')

# Display the columns of the housing data DataFrame 
housing_data.columns

# Display descriptive statistics of the 'SalePrice' column in the housing data.
housing_data['SalePrice'].describe()

# Create a histogram to visualize the distribution of 'SalePrice'
sns.displot(housing_data['SalePrice'])
plt.show()
plt.clf()

# Calculate the skewness of the log-transformed 'SalePrice' and display a histogram
log_data = np.log(housing_data['SalePrice'])
print(log_data.skew())
sns.displot(log_data)
plt.show()
plt.clf()

# Create a scatter plot to show the relationship between '1stFlrSF' and 'SalePrice'
data = pd.concat([housing_data['SalePrice'], housing_data['1stFlrSF']], axis=1)
data.plot.scatter(x='1stFlrSF', y='SalePrice', ylim=(0,800000))
plt.show()
plt.clf()

# Create a scatter plot to show the relationship between 'GarageArea' and 'SalePrice'
data = pd.concat([housing_data['SalePrice'], housing_data['GarageArea']], axis=1)
data.plot.scatter(x='GarageArea', y='SalePrice', ylim=(0,800000))
plt.show()
plt.clf()

# Create a boxplot to visualize the relationship between 'YearBuilt' and 'SalePrice'
data = pd.concat([housing_data['SalePrice'], housing_data['YearBuilt']], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x='YearBuilt', y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000)
plt.xticks(rotation=90)
plt.show()
plt.clf()
