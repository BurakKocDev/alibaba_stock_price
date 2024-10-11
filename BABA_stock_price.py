import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score
import warnings 
warnings.simplefilter("ignore")


df = pd.read_csv("BABA.CSV")
print(df.head(5))
print(df.columns)
print(df.shape)
print(df.isnull().sum())


missing_values = df.isnull().sum()
data_types = df.dtypes

print(missing_values,data_types)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes
)
# Calculate descriptive statistics for the dataset
descriptive_statistics = df.describe()

# Display the descriptive statistics
print(descriptive_statistics)



# Set the style of matplotlib
plt.style.use('seaborn-v0_8-darkgrid')

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(14, 18), sharex=True)

# Plotting price data
axes[0].plot(df['Date'], df['Open'], label='Open', color='blue')
axes[0].plot(df['Date'], df['High'], label='High', color='green')
axes[0].plot(df['Date'], df['Low'], label='Low', color='red')
axes[0].plot(df['Date'], df['Close'], label='Close', color='purple')
axes[0].set_title('Alibaba Stock Prices: Open, High, Low, Close')
axes[0].set_ylabel('Price (USD)')
axes[0].legend()

# Plotting adjusted close price
axes[1].plot(df['Date'], df['Adj Close'], label='Adjusted Close', color='orange')
axes[1].set_title('Alibaba Adjusted Close Price')
axes[1].set_ylabel('Adjusted Price (USD)')
axes[1].legend()

# Plotting volume
axes[2].bar(df['Date'], df['Volume'], color='grey')
axes[2].set_title('Alibaba Trading Volume')
axes[2].set_ylabel('Volume')
axes[2].set_xlabel('Date')

# Tight layout to ensure no overlap
plt.tight_layout()

# Show the plots
plt.show()


"""Stock Prices (Open, High, Low, Close):

The first plot displays the daily opening, highest, lowest, and closing stock prices. You can see the variations and trends over time, giving back the market behavior and events affecting stock prices.

Adjusted Close Price:

The second plot presents adjusted closing price, which accounts for corporate actions.This is often used for performance analysis over time.

Trading Volume:

The third plot shows the trading volume, indicating the number of shares traded each day. High volume days often linked with significant price movements or news events."""



# moving averages calculation
df['30_day_MA'] = df['Close'].rolling(window=30).mean()
df['90_day_MA'] = df['Close'].rolling(window=90).mean()

# Plotting the moving averages along with the close price
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue', alpha=0.5)
plt.plot(df['Date'], df['30_day_MA'], label='30-Day Moving Average', color='red')
plt.plot(df['Date'], df['90_day_MA'], label='90-Day Moving Average', color='green')
plt.title('30-Day and 90-Day Moving Averages of Alibaba Close Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()



#Specific Time Period Analysis for 2020¶


# Specific time period analysis for the first half of 2020
start_date = '2020-01-01'
end_date = '2020-06-30'
period_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Plotting the close price for this period
plt.figure(figsize=(14, 7))
plt.plot(period_df['Date'], period_df['Close'], label='Close Price', color='blue')
plt.title('Alibaba Close Price During First Half of 2020')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()


"""The plot shows Alibaba's stock close price during the initial months of the COVID-19 pandemic (January to June 2020).
 This period captures the market's reaction to the onset of the pandemic,
 with visible volatility and significant price movements during March and April 2020."""
 
 
 
 # Calculating daily percentage change
df['Daily_Change'] = df['Close'].pct_change() * 100

# Plotting the distribution of daily changes
plt.figure(figsize=(14, 7))
plt.hist(df['Daily_Change'].dropna(), bins=50, color='navy', alpha=0.7)
plt.title('Distribution of Daily Percentage Changes in Alibaba Close Price')
plt.xlabel('Percentage Change')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


"""the histogram helps us understand the volatility of the stock price. 
Most daily changes cluster near zero, indicating many days with minor price changes.there are also tails on both sides, indicating days with significant price increases and decreases, especially around the start of the pandemic."""


#xgboost model


#df['Date'] = pd.to_datetime(df['Date'])


# Select relevant features
features = ['Open', 'High', 'Low', 'Volume', 'Adj Close']
target = 'Close'

# Split the data into features (X) and target (y)
X = df[features]
y = df[target]

cutoff = int(len(df) * 0.8)

X_train = X[:cutoff]
X_test = X[cutoff:]
y_train = y[:cutoff]
y_test = y[cutoff:]



# Check the shapes of the splits
X_train.shape, X_test.shape, y_train.shape, y_test.shape


from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score
# Initialize the XGBoost regressor
xgb_model = XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, random_state=42)

# Train the model on the training data
xgb_model.fit(X_train, y_train)

# Predict on the testing data
y_pred = xgb_model.predict(X_test)

# Calculate performance metrics
rmse = mean_squared_error(y_test, y_pred, squared=False)
mape = mean_absolute_percentage_error(y_test, y_pred)*100
r2 = r2_score(y_test, y_pred)

print("rmse :",rmse)
print("mape :",mape)
print("r2 :",r2)



#baba predication plot 

date = df['Date']

plt.figure(figsize=(14, 7))
plt.plot(date[:cutoff], y_train, label='Close Price', color='blue', alpha=0.5)
plt.plot(date[cutoff:], y_test, label='test', color='red')
plt.plot(date[cutoff:], y_pred, label='prediction', color='green')
plt.title('Ali Baba Close price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()



plt.figure(figsize=(14, 7))
plt.plot(date[cutoff:], y_test, label='test', color='red')
plt.plot(date[cutoff:], y_pred, label='prediction', color='blue')
plt.title('prrediction vs test')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()