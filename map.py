import pandas as pd
import folium
from geopy.geocoders import Nominatim
import time

# Load the dataset
file_path = 'wing_tree.csv'  # Replace with your actual file path
family_tree_df = pd.read_csv(file_path)

# Clean the Birthplace data
family_tree_df = family_tree_df[family_tree_df['Birthplace'].notna()]
birthplaces = family_tree_df['Birthplace'].unique()
birthplaces = [place for place in birthplaces if place not in ["", " ", "\"", "Unknown"]]

# Grouping by birthplace
grouped_data = family_tree_df.groupby('Birthplace').apply(lambda x: x[['Name', 'Birth_Year']].to_dict('records'))

# Initialize the geolocator
geolocator = Nominatim(user_agent="family_tree_geocoder")

# Geocode the birthplaces (this may take some time)
locations = {}
for place in birthplaces:
    try:
        location = geolocator.geocode(place)
        if location:
            locations[place] = (location.latitude, location.longitude)
        time.sleep(1)  # To avoid overloading the geocoding service
    except Exception as e:
        print(f"Error geocoding {place}: {e}")

# Create a map
map = folium.Map(location=[20, 0], zoom_start=2)

# Add markers to the map
for place, coords in locations.items():
    popup_text = f"{place}<br>"
    for person in grouped_data.get(place, []):
        popup_text += f"{person['Name']} ({person['Birth_Year']})<br>"
    folium.Marker(location=coords, popup=popup_text).add_to(map)

# Save the map to an HTML file
map.save('birthplaces_map.html')
