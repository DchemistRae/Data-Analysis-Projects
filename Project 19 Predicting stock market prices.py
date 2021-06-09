'''
Guided Project: Prdicting Stock Market 
We will be running this project on a python terminal.

n this project, we'll work with data from the S&P500 Index data from 1950 to 2015. The S&P500 is a stock market index that tracks the performance of the American stock market. The index includes 500 of the largest (not necessarily the 500 largest) companies whose stocks trade on either the NYSE or NASDAQ.
'''


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from datetime import datetime

# Import df and parse_dates
df =pd.read_csv('sphist.csv')

# Parse date column as datetime
df['Date'] =  pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True, ascending = True)

# View dataframe 
print(df.head(3))

'''
Our stock market dataframe is a timeseries data. we can generate indicators to make our model more accurate. For instance, we can create a new column that contains the average price of the last 10 trades for each row. This incorporates information from multiple prior rows into one and makes predictions much more accurate.

However, for this project. We will create indicators for:
The average price from the past 5 days.
The average price for the past 30 days.
The average price for the past 365 days.
'''
# Create indicators using the inbuilt pandas rolling function
#get the day_5 col
df['day_5'] = df['Close'].rolling(window=5).mean().shift(1, axis=0)

#get the day_30 col
df['day_30'] = df['Close'].rolling(window=30).mean().shift(1, axis=0)

#get the day_365 col
df['day_365'] = df['Close'].rolling(window=365).mean().shift(1, axis=0)

'''
Using the rolling function, rows without enough data to calculate indices will be saved as nans, we need to delete all rows with nan. The past year average uses 365 days of historical data and the dataset starts on 1950-01-03. Thus, any rows that fall before 1951-01-03 don't have enough data and should be deleted.
'''

#Check for and drop all rows with missing values
#print(df.isnull().sum())
df.dropna(axis = 0, inplace =True)
#print(df.isnull().sum()) #check to make sure there is no more missing values
# Create a train and test dataset
train = df[df['Date'] < datetime(year = 2013, month = 1, day = 1)]
test = df[df['Date'] > datetime(year = 2013, month = 1, day = 1)]

'''
Now, a linear model will be used to model and predict the closing price. And our error matric for performance accessing will be the mean_absolute_error (MAE) and mean_squared_error (MSE). We will only be using the three new columns we added to our dataset
'''

features = ['day_5', 'day_30', 'day_365']
target = ['Close']
lr = LinearRegression()

# Train and test model
model =lr.fit(train[features], train[target])
preds = model.predict(test[features])
mae = mean_absolute_error(test[target], preds)
mse = mean_squared_error(test[target], preds)
print('MAE: {}'.format(np.average(mae))) #16.142439643554464
print('MSE: {}'.format(np.average(mse))) #493.731303012588

'''
Conclusion

This project is a minimalistic LinearRegression model, fitted and tested on the metric of MAE. It was completely carried out using the python terminal. After fitting and testing this model. The error metric MAE = 16.142439643554464 and MSE = 493.731303012588.
'''
