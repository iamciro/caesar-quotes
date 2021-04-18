"""
    This file contains utils functions
"""
import requests
import json

API_END_POINT = "https://caesar-api.herokuapp.com/quote"

def get_quote():
    """
        Get quote from API
    """
    try:
        response = requests.get(API_END_POINT)
        data = json.loads(response.text)
        return data['quote']
    except KeyError:
        return None
    except requests.exceptions.ConnectionError:
        return None