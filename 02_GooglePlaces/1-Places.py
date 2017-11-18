# Dependencies
import requests
import json

# Google developer API key
gkey = "{YOUR API KEY HERE}"

# Target city
target_city = {"lat": 43.6187102, "lng": -116.2146068}
target_search = "Chinese"
target_radius = 8000
target_type = "restaurant"

# Build the endpoint - Search for Chinese Restaurant within 8000 Meters of
# Boise
target_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" \
    "?keyword=%s&location=%s,%s&radius=%s&types=%s&key=%s" % (
        target_search, target_city["lat"], target_city["lng"], target_radius,
        target_type, gkey)

# Print the assembled URL
print(target_url)
