import requests
from jarvis_ip import get_public_ip
import os
from dotenv import load_dotenv, find_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Your RapidAPI Key
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

# Base URL for the WeatherAPI
BASE_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

def get_weather(q):
    """Get the current weather for a city/state, GPS coordinates, an address, or an IP address."""
    params = {
        "q": q
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    # Check if the response was successful
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()  # This will contain the error information.

# I am not sure how to create functions without parameters since it
# anytime I do it says invalid json in the assitant creator.
# For now we just ignore what ever it sends us.
def get_local_weather(q):
    return get_weather(get_public_ip())

