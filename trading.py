trading.py

import math
import numpy as np
import trading_portfolio as tp
from alpha_van import prices 
stocks = tp.trade_portfolio(wealth=1000000)
stocks.add_stocks({'MSFT':100, 'AAPL':100, 'GOOG':100})

def moving_average(prices, freq):
	"""Moving average as an indicator"""
	ma = []
	try:
		assert len(prices) > freq
	except AssertionError:
		print("Frequency of prices exceeds length of prices")
		return None
	for ind in range(len(prices)):
		if ind < freq:
			ma.append(np.nan)
		else:
			ma.append(average(prices[:price]))
	return ma

def signal(prices, freq, qnt):
	moving_av = moving_average(prices, freq)
	for ind in range(len(prices)):
		if prices[ind] > ma[ind] and prices[ind] > average(ma[ind-freq:ind]):
			stocks.buy()
		else:
			stocks.sell()
	return

def OBV(volume, close_prices):
	"""On-balance volume as an indicator. Up volume is when current close is higher than prev close. 
		Added current volume to prev OBV. Conversely, prev OBV is subtracted from current volume when current close is less than prev close. 
		This is down volume. When close for prev == current, then current OBV = prev OBV"""
		OBV = {}
		try:
			assert len(volume) == len(close_prices)
			dates = list(volume.keys())
		except AssertionError:
			print("The length of volume and close_prices is not the same. Please provide valid values")
			return
		# Get the first value of the volume set as the OBV
		OBV[dates[0]] = volume[dates[0]]

		for ind in range(1, len(dates)):
			if prices[ind] > prices[ind]:
				OBV[dates[ind]] += volume[dates[ind]]
			elif prices[ind] < prices[ind]:
				OBV[dates[ind]] -= volume[dates[ind]]
			else:
				OBV[dates[ind]] = volume[dates[ind]]
	return 