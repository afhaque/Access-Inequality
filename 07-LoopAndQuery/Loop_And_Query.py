# Dependencies
import numpy as np
import pandas as pd
from census import Census
from us import states
import requests

# Census API Key
c = Census("85ac64b6b5a9c0901b00329d1ef41f0c53ccfc98", year=2015)

# Retrieve Census Data (Reference: https://gist.github.com/afhaque/60558290d6efd892351c4b64e5c01e9b)
zip_census = c.acs5.get(( "B19013_001E",
                          "B19301_001E",
                          "B15003_002E",
                          "B15003_017E",
                          "B15003_018E",
                          "B15003_022E",
                          "B15003_021E",
                          "B15003_023E",
                          "B15003_024E",
                          "B15003_025E",
                          "B17001_002E",
                          "B23025_002E",
                          "B23025_005E",
                          "B01002_001E",
                          "B01002_002E",
                          "B01002_003E",
                          "B01003_001E",
                          "B25064_001E",
                          "B25077_001E",
                          "B25077_001E",
                          "B02001_002E",
                          "B02001_003E",
                          "B02001_004E",
                          "B02001_005E",
                          "B03001_003E"), {'for': 'zip code tabulation area:*'})

# Convert to DataFrame
zip_census = pd.DataFrame(zip_census)

# Column Reordering
zip_census = zip_census.rename(columns={"B19013_001E": "Household Income", 
                                      "B19301_001E": "Income Per Capita",
                                      "B15003_002E": "Education None",
                                      "B15003_017E": "Education High School",
                                      "B15003_018E": "Education GED",
                                      "B15003_022E": "Education Bachelors",
                                      "B15003_021E": "Education Associates",
                                      "B15003_023E": "Education Masters",
                                      "B15003_024E": "Education Professional",
                                      "B15003_025E": "Education Doctorate",
                                      "B17001_002E": "Poverty",
                                      "B23025_002E": "Employment Labor Force",
                                      "B23025_005E": "Employment Unemployed",
                                      "B01002_001E": "Median Age",
                                      "B01002_002E": "Median Male Age",
                                      "B01002_003E": "Median Female Age",
                                      "B01003_001E": "Population",
                                      "B25064_001E": "Median Gross Rent",
                                      "B25077_001E": "Median Home Value",
                                      "B02001_002E": "White Population",
                                      "B02001_003E": "Black Population",
                                      "B02001_004E": "Native American Population",
                                      "B02001_005E": "Asian Population",
                                      "B03001_003E": "Hispanic Population",
                                      "zip code tabulation area": "zipcode"})

# Visualize Data
print(zip_census)

# Merge Data
zip_census_geocoded = zip_census.merge(zip_lat_lng, on="zipcode", how="left")
print(zip_census_geocoded)

# Filter to Single State
zip_data = zip_census_geocoded[zip_census_geocoded["state"] == "WV"]
print(zip_data)

# Build the URLs
max_distance_meters = 8000
city_amenity = "Hospial"
gkey = "{API KEY}"
zip_data["Google_URL"] = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location=" + zip_census_geocoded["lat"].map(str) + "," + zip_census_geocoded["lng"].map(str) + "&radius=" + str(max_distance_meters) + "&keyword=" + city_amenity + "&key=" + gkey
print(zip_data)

# Query the URLs
# Sample Test
test_run = zip_data.sample(n=15)
test_run["Count"] = ""

# Loop through and run Google search to get counts for each record 
for index, row in test_run.iterrows():

        # Create endpoint url using Google Places Radar and the lat/lng we identified earlier
        target_url ="https://maps.googleapis.com/maps/api/place/radarsearch/json?location=%s,%s&radius=8000&type=bank&key=%s" % (test_run.loc[index]["lat"], test_run.loc[index]["lng"], gkey)

        # This link helps to handily see the JSON generated for each query
        print("Now retrieving city #%s: %s" % (row_count, test_run.loc[index]["zipcode"]))
        row_count += 1 
        print(target_url)

        # Run a request to grab the JSON at the target URL
        radar_data = requests.get(target_url).json()

        # Measure radar_data count on the number of results in the retrieved area
        count = len(radar_data["results"])

        print("Final Count: " + str(count))
        print("")

        # Store the bank count into the Data Frame
        test_run.set_value(index, "Count", count)

        # Reset bank_count (so there is no chance that a previous record is influencing a latter one)
        count = 0

        # Add to Row Count for test             
        row_count = row_count + 1


# Visualize
test_run.head()
