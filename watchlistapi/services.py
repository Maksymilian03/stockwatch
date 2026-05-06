import os
import requests
from dotenv import load_dotenv
from datetime import timedelta
from django.core.cache import cache




load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_stock_price(symbol):
    cache_price = cache.get(f"stock_price_{symbol}")
    if cache_price is not None:
        return cache_price
    

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    
    try:
        response = requests.get(url)
        data = response.json()
        price = float(data['Global Quote']['05. price'])
    except KeyError:
        return None
    except ConnectionError:
        return None
    except Exception as e:
        return None
    else:
        cache.set(f"stock_price_{symbol}", price, 3600)
        return price


def get_stock_price_at_date(symbol, date):
    cache_price = cache.get(f"stock_price_{symbol}_{date}")
    if cache_price is not None:
        return cache_price
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    try:
        response = requests.get(url)
        data = response.json()

        price_at_end_of_day = data['Time Series (Daily)'][date]['4. close']
    except (KeyError, ConnectionError):
        return None
    else:
        cache.set(f"stock_price_{symbol}_{date}", price_at_end_of_day, 3600)
        return price_at_end_of_day


def get_last_business_day(date):
    if date.weekday() == 5:
        return date - timedelta(days=1)
    elif date.weekday() == 6:
        return date - timedelta(days=2)
    else:
        return date




if __name__ == '__main__':
    

    get_stock_price('AAPL')