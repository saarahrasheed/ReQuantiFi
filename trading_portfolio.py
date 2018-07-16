trading_portfolio.py
import numpy as np
import time
from datetime import datetime as dt
from collections import OrderedDict
from alpha_van import prices

# Import prices from local directory or access through API in real time
# Ensure that timestamps are present with the prices inclusive of date and time

class trade_portfolio:
	def __init__(self):
		self.stocks = []
		self.shares = {}
		self.buy_side = {}
		self.sell_side = {}
		self.transactions_log = OrderedDict()
		self.sell_log = []
		self.buy_log = []
		self.wealth = total_worth()

	def add_stocks(self, companies_with_shares):
		new_companies = []
		for company in companies_with_shares:
			if company in self.shares:
				self.shares[company] += companies_with_shares[company]
			else:
				self.shares[company] = companies_with_shares[company]
				new_companies.append(company)
		add_companies(new_companies)

	def add_companies(self, new_companies):
		self.stocks.extend(new_companies)

	def check_companies(self):
		try:
			assert self.stocks == list(self.shares.keys())
		except AssertionError:
			for stock in stocks:
				if stock not in self.shares.keys():
					self.shares[stock] = np.nan
			print("Companies added with nan as shares.")
		print("Validated!")

	def total_worth(self):
		net_worth = 0
		for company in self.shares:
			net_worth += self.shares[company]*prices[company]
		return net_worth

	def buy(self, stock, shares=1):
		try:
			self.shares[stock]
		except KeyError:
			print("Stock does not exist in portfolio")

		self.shares[stock] += shares
		timest = get_time_stamp()
		self.transactions_log[timest] = 'BUY'
		self.buy_log.append(timest)

	def sell(self, stock, shares=1):
		try:
			self.shares[stock]
			assert self.shares[stock] > shares
		except KeyError:
			print("Stock does not exist in portfolio")
		except AssertionError:
			print("Not enough shares to sell")
		self.shares[stock] -= shares
		timest = get_time_stamp()
		self.transactions_log[timest] = 'SELL'
		self.sell_log.append(timest)

	def holding_period(self, first_to_first=True):
		if first_to_first is True:
			first_buy = sell_log[0]
			first_sell = buy_log[0]
		else:
			first_buy = buy_log[0]
			first_sell = sell_log[-1]
		try:
			assert first_sell > first_buy
		except AssertionError:
			print('Is short selling allowed on this platform?')

	def holding_period_returns(self):
		return

	def get_time_stamp():
		return dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


