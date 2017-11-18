# Dependencies
import requests
import json

# Google developer API key
gkey = "{YOUR API KEY HERE}"

# Target city
target_city = "Boise, Idaho"

# Build the endpoint URL
target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
    "?address=%s&key=%s" % (target_city, gkey)

# Print the assembled URL
print(target_url)

# Run a request to endpoint and convert result to json
geo_data = requests.get(target_url).json()

# Print the json (pretty printed)
print(json.dumps(geo_data, indent=4, sort_keys=True))

# Extract latitude and longitude
lat = geo_data["results"][0]["geometry"]["location"]["lat"]
lng = geo_data["results"][0]["geometry"]["location"]["lng"]

# Print the latitude and longitude
print("%s: %s, %s" % (target_city, lat, lng))
