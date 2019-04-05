import requests
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
import time
import json

# This script will check a Lowes location for a particular item and tell you how many of that item are currently in stock.

url = "https://www.lowes.com/pd/search/3069739/pricing/0655" #Replace 3069739 with the item name and 0655 with the store number
response = requests.get(url, timeout=None)
soup = BeautifulSoup(response.content, "html.parser")
jstext = soup.find('script', type="text/javascript").text.strip()
arr = jstext.split(';')
result = arr[2].split('=')
jsontxt = json.loads(result[1])
print(jsontxt['pickup']['availabileQuantity'])
