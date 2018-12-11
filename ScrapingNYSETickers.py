# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:20:00 2018

@author: saarah.rasheed
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import csv
# run chromedriver from cmd before you run this

url = 'https://www.nyse.com/listings_directory/stock'


def scrapingNYSE():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    # A dismiss option pops up
    try:
      driver.find_element_by_class_name('close').click()
    except NoSuchElementException:
      print('Nothing to dismiss!')
    tickers = []
    security_names = []
    isPossible = True
    while isPossible:
        data = driver.find_elements_by_xpath('//td')
        row_number = 0
        for d in data:
            row_number += 1
            if row_number % 2 == 0:
                security_names.append(d.text)
            else:
                tickers.append(d.text)
        print('Completed this page!')
        try:
            driver.find_elements_by_xpath("//a[@rel='next']")[-1].click()
        except IndexError:
            print('Reached the last page!')
            isPossible = False
        sleep(0.5)
    ticker_name_mapping = {ticker: name for ticker, name in zip(tickers, security_names)}
    return ticker_name_mapping


def writeToCSV(ticker_name_mapping, name='Tickers.csv'):
    assert isinstance(ticker_name_mapping, dict)
    with open(name, 'w') as f:
        for tick in ticker_name_mapping:
            f.write(tick + ',' + ticker_name_mapping[tick])
            f.write('\n')
    f.close()
    return


