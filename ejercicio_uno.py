import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file as a dataframe and set the "Date" column as the index
data = pd.read_csv("BTC-USD.csv", usecols=["Date", "Close"], index_col="Date")

# Number of days
d = int(input('digite el número de días '))

# Calculate the moving average using the rolling() function
ma = data.Close.rolling(d).mean()

# Calculate the slope and intercept of the linear regression line
m, b = np.polyfit(np.arange(d-1, len(ma)), ma.dropna(), deg=1)

# Plot the data and the linear regression line
plt.plot(np.arange(d-1, len(ma)), ma.dropna(), 'o', label='Data')
plt.plot(np.arange(d-1, len(ma)), m*np.arange(d-1, len(ma))+b, label='Linear Regression')
plt.xlabel('Day')
plt.ylabel('Price')
plt.legend()
plt.show()
