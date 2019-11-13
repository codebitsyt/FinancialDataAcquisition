'''
Requirements:
Pandas: https://pandas.pydata.org/getpandas.html
Fixed Yahoo Finance: https://pypi.org/project/yfinance/
'''

#import neccessary packages/modules
import datetime
import yfinance as yf 
from pandas_datareader import data as pdr
yf.pdr_override()

# Define our respective start and end dates for time series data
start,end = datetime.datetime(1980,1,1), datetime.date.today()

# Define our ticker shortcode as a string (MSFT) and use yahoo finance's Ticker function parsing argument as the ticker string.
ticker = "MSFT"
tick = yf.Ticker(ticker)

# Store our time-series data as a new variable data
data = pdr.get_data_yahoo(ticker,start,end)

# Get and store dividends and ticker info into variables dividends and info respectively
dividends,info = tick.dividends,tick.info

# Print time-series data, dividends and info for our ticker all on new lines.
print(data,'\n',dividends,'\n\n',info,'\n')