import os
from decimal import Decimal, ROUND_CEILING
import requests
import tomllib
from dotenv import load_dotenv

load_dotenv()

def load_config():
    """Load Toml data from file"""
    with open("config.toml", "rb") as f:
        return tomllib.load(f)

def get_amount_rate(currency):
    try:
        key = os.getenv("API_KEY")
        response = requests.get(f"https://api.fastforex.io/fetch-one?api_key={key}&from={currency}&to=GEL")
        response.raise_for_status()
        
        data = response.json()
        return data["result"]["GEL"]
    except requests.exceptions.RequestException : 
        print("Cannot get rate information")
        
def ceil(number, ndigits=0):
    d = Decimal(str(number))
    target = Decimal('1e-' + str(ndigits)) if ndigits > 0 else Decimal('1')
    return float(d.quantize(target, rounding=ROUND_CEILING))

    
