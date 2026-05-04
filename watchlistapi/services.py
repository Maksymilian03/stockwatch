import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_stock_price(symbol):
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
        
       return price
