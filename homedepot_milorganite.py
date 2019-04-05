import json
import requests
import urllib

# This script will pull inventory data from The Home Depot and determine if it's in stock or not.

url = urllib.request.urlopen("https://www.homedepot.com/p/svcs/frontEndModel/100618523?_=1554485255527") # 100618523 is the item number. 1554485255527 is somehow tied to the store ID.
content = url.read()
data = json.loads(content)
print(data['primaryItemData']['itemAvailability']['inventoryStatus'])
