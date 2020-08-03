
# import modules pandas and os
import pandas as pd
import os

# file path to open city data
cities_data = os.path.join("data", "city_weather_data.csv")

# Read city data file and store in dataframe
cities_data_df = pd.read_csv(cities_data)

#set index to City Name
cities_data_df = cities_data_df.set_index('City Name')


cities_data_df.to_html('city_data.html')


