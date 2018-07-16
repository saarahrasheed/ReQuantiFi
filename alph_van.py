# coding=utf-8

import requests as r
# different functions available, can be added as a list to iterate over.
# For daily adjusted: TIME_SERIES_DAILY_ADJUSTED
# For batch of 100 symbols to return latest price: BATCH_STOCK_QUOTES [enter symbols separated by commas]
param_function = 'TIME_SERIES_INTRADAY'

# interval may be 1, 5 , 15, 30 or 60 minutes
interval = '1min'
# output size can be compact: last 100 data points or full: full-length intra day time series
output_size = 'compact'
# data type may be json or csv
data_type = 'json'
# Replace YOURKEY with the api_key that can be obtained through Alpha Vantage website.
api_key = YOURKEY

def get_minute_data(symbol, price_type='close'):
	url = 'http://www.alphavantage.co/query?function='+param_function+'&symbol='+symbol+'&interval='+interval+'&apikey='+api_key+'&datatype='+data_type
	response = r.get(url)
	time_series = response.json()['Time Series (1min)']
	open_price = {}
	high_price = {}
	low_price = {}
	close_price = {}
	volume = {}
	for date in time_series.keys():
	    open_price[date] = time_series[date]['1. open']
	    high_price[date] = time_series[date]['2. high']
	    low_price[date] = time_series[date]['3. low']
	    close_price[date] = time_series[date]['4. close']
	    volume[date] = time_series[date]['5. volume']

	if price_type.lower() == 'close':
		return close_price
	elif price_type.lower() == 'open':
		return open_price
	elif price_type.lower() == 'high'
		return high_price
	elif price_type.lower() == 'low':
		return lower
	elif price_type.lower() == 'volume':
		return volume
	else:
		return None 

symbols = ['AAPL', 'MSFT', 'GOOG']

prices = {}
for symbol in symbols:
	prices[symbol] = get_minute_data(symbol=symbol)


# def get_realtime_data(symbol, type='close'):
# 	# Use some sort of update function to update the incoming data every now and then.
# 	# All methods that are applicable here should be instance wise. That is, per value comparison in OBV and so on.
# 	return
