# Allows access to yahoo finance api
import yfinance as yf
# Basic imports
import pandas as pd
import numpy as np
# Allows for access to terminal notifications
import os

def get_stock_data(stock_list):
    """
    Functino to pull and format live stock data 
    
    Parameters:
        stock_list (list): list of stock tickers
    """
    result = ""
    # Get stock data
    for i in stock_list:
        stock_info = yf.Ticker(i).info
        market_price = stock_info['regularMarketPrice']
        result += i + ':' + str(market_price) + '  '
    return result

def notify(title, subtitle, message):
    """
    Functino to format and send terminal notifications

    Parameters:
        title (str): title of notification
        subtitle (str): subtitle of notification
        message (str): message of notification
    """
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Enter the Ticker Symbols of the stocks you are interested in 
stock_list = ['TSLA', 'AAPL', 'AMZN', 'GOOGL', 'FB']

# Calling the function (This might take a few minute)
notify(title='Daily Stock update',
       subtitle='Live price of your stocks',
       message=get_stock_data(stock_list))