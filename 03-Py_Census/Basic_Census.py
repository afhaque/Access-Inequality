# Dependencies
import numpy as np
import pandas as pd
from census import Census
from us import states

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