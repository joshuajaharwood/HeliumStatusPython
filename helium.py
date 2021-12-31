'''
TODO: Logging to CSV
TODO: Refactor in to functions
TODO: Handle non-200 timeouts

- Joshua J. A. Harwood
'''

import requests
import json

url = "https://api.helium.io/v1/accounts/13kvrLETZfhp8P9t3N79gtr47bxn2iWMYzSFp6gNZPeNPg3TgHb/hotspots"

response = requests.get(url)

# For successful API call, response code will be 200 (OK)
if(response.ok):
    data = json.loads(response.content)
    # Remove root node
    data = data["data"] 

    print("{0} hotspots found.\n".format(len(data)))
    
    for hotspot in data:
      hotspotBlock = hotspot["status"]["height"]
      blockchainBlock = hotspot["block"]
      percentage = (hotspotBlock / blockchainBlock) * 100
      delta = blockchainBlock - hotspotBlock

      print("Hotspot: {:}".format(hotspot["name"]))
      print("Online status: {:}".format(hotspot["status"]["online"]))
      print("Sync status: {:}/{:} ({:.2f}%, {:} blocks to go)".format(hotspotBlock, blockchainBlock, percentage, delta))
      print("\n")
else:
  # If response code is not ok (200), print the resulting http error code with description
    response.raise_for_status()