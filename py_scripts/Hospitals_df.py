#!/usr/bin/env python
# coding: utf-8

# In[41]:


import requests
import json
import pandas as pd
import numpy as np
from config import geoapify_key
from py_scripts.Master_df import Master_NC_Dataframe
print(Master_NC_Dataframe.columns)


# In[16]:


# List of place IDs to iterate over
place_ids = Master_NC_Dataframe["place_id"].tolist()

geoapify_places_url = "https://api.geoapify.com/v2/places?"
# List to store the JSON responses
i = 0
responses = []
for place_id in place_ids:
    # Parameters for the API request
    params = {
        "categories": "healthcare.hospital",
        "filter": f"place:{place_id}",
        "limit": "500",
        "apiKey": geoapify_key  # replace with actual API key
    }
    # Make the request
    response = requests.get(geoapify_places_url, params=params)
    
    if response.status_code == 200:
        # Append the JSON response to the list
        responses.append(response.json())
        i = i + 1
        print(f"Processing record {i} of {len(place_ids)}")
    else: 
        print(f"Error: {response.status_code}")
        break

# Save the list of responses to a JSON file
with open('Resources/geoapify_county_hospitals.json', 'w') as f:
    json.dump(responses, f)
    


# In[31]:


#create a dataframe with the data from the API call
#normailze the data
#json dump responses
# Load the json file
with open("Resources/geoapify_county_hospitals.json") as f:
    data = json.load(f)

# Define the record path
record_path = ['features', 'properties']

# Extract the nested data into a DataFrame
df_list = []
# For each 'FeatureCollection' in your data
for feature_collection in data:
    # Check if there are any 'features' in the 'FeatureCollection'
    if feature_collection['features']:
        # For each 'feature' in 'features', normalize the 'properties' dictionary and append it to df_list
        for feature in feature_collection['features']:
            df_list.append(pd.json_normalize(feature['properties']))

# Concatenate all the dataframes in the list into a single dataframe
hospitals_geoapify_df = pd.concat(df_list, ignore_index=True)



columns = [
    'county',
    'city',
    'name',
    'postcode',
    'lon',
    'lat',
    'formatted',
    'categories',
    'place_id',
    'datasource.raw.name',
    'datasource.raw.phone',
    'datasource.raw.website'
    ]
hospitals_geoapify_df = hospitals_geoapify_df[columns]
hospitals_geoapify_df.rename(columns={'county': 'County', 'city': 'Hospital City', 'name': 'Hospital Name', 'postcode': 'Hospital Zipcode', 'formatted': 'Hospital Address', 'categories': 'Hospital Geoapify Category', 'place_id': 'Hospital Place ID', 'datasource.raw.name': 'Source Hospital Name', 'datasource.raw.phone': 'Hospital Phone', 'datasource.raw.website': 'Hospital Website'}, inplace=True)
hospitals_geoapify_df['Hospital Name'].fillna('No Name Given - Possible branch of main Hospital', inplace=True)
print(hospitals_geoapify_df.head())
hospitals_geoapify_df.to_csv("Clean_Resources/hospitals_geoapify.csv", index=False)


# In[42]:


from config import NC_osbm_key
base_url = "https://linc.osbm.nc.gov/api/records/1.0/search/?"
headers = {
    "Authorization": f"Apikey {NC_osbm_key}"
}
params = {
    "dataset": "vital-statistics-and-health-linc",
    "q": "",
    "rows": 9000,
    "facet": ["area_name", "area_type", "year", "variable"],
    "refine.area_type": "County",
    "refine.year": "2020",
    "offset+limit": "9000"
}

response = requests.get(base_url, params=params, headers=headers).json()
response
print(json.dumps(response, indent=4, sort_keys=True))


# In[43]:


#put into .json file with proper formatting
data_list = [record['fields'] for record in response['records']]
with open('Resources/vital_stats_linc.json', 'w') as json_file:
    json.dump(data_list, json_file)

#read json file
vital_stats = pd.read_json("Resources/vital_stats_linc.json")
print(vital_stats.head())
print(len(vital_stats))


# In[44]:


from config import NC_osbm_key
base_url = "https://linc.osbm.nc.gov/api/records/1.0/search/?"
headers = {
    "Authorization": f"Apikey {NC_osbm_key}"
}
params = {
    "dataset": "education",
    "q": "",
    "rows": 9000,
    "facet": ["area_name", "area_type", "year", "variable"],
    "refine.area_type": "County",
    "refine.year": "2020",
    "offset+limit": "9000"
}

response = requests.get(base_url, params=params, headers=headers).json()
response
print(json.dumps(response, indent=4, sort_keys=True))


# In[45]:


#put into .json file with proper formatting
data_list = [record['fields'] for record in response['records']]
with open('Resources/education_stats_linc.json', 'w') as json_file:
    json.dump(data_list, json_file)

#read json file
ed_stats = pd.read_json("Resources/education_stats_linc.json")
print(ed_stats.head())
print(len(ed_stats))


# In[46]:


from config import NC_osbm_key
base_url = "https://linc.osbm.nc.gov/api/records/1.0/search/?"
headers = {
    "Authorization": f"Apikey {NC_osbm_key}"
}
params = {
    "dataset": "employment-and-income-linc",
    "q": "",
    "rows": 9000,
    "facet": ["area_name", "area_type", "year", "variable"],
    "refine.area_type": "County",
    "refine.year": "2020",
    "offset+limit": "9000"
}

response = requests.get(base_url, params=params, headers=headers).json()
response
print(json.dumps(response, indent=4, sort_keys=True))


# In[47]:


#put into .json file with proper formatting
data_list = [record['fields'] for record in response['records']]
with open('Resources/employment_income_stats_linc.json', 'w') as json_file:
    json.dump(data_list, json_file)

#read json file
employment_stats = pd.read_json("Resources/employment_income_stats_linc.json")
print(employment_stats.head())
print(len(employment_stats))


# In[48]:


from config import NC_osbm_key
base_url = "https://linc.osbm.nc.gov/api/records/1.0/search/?"
headers = {
    "Authorization": f"Apikey {NC_osbm_key}"
}
params = {
    "dataset": "pop_migration",
    "q": "",
    "rows": 9000,
    "facet": ["area_name", "area_type", "variable", "year", "data_type"],
    "refine.area_type": "County",
    "refine.data_type": "Count",
    "refine.year": "2020",
    "offset+limit": "9000"
}

response = requests.get(base_url, params=params, headers=headers).json()
response
print(json.dumps(response, indent=4, sort_keys=True))


# In[49]:


#put into .json file with proper formatting
data_list = [record['fields'] for record in response['records']]
with open('Resources/pop_migration_linc.json', 'w') as json_file:
    json.dump(data_list, json_file)

#read json file
pop_migration = pd.read_json("Resources/pop_migration_linc.json")
print(pop_migration.head())
print(len(pop_migration))


# In[50]:


from config import NC_osbm_key
base_url = "https://linc.osbm.nc.gov/api/records/1.0/search/?"
headers = {
    "Authorization": f"Apikey {NC_osbm_key}"
}
params = {
    "dataset": "population-by-age-race-sex-linc",
    "q": "",
    "rows": 10000,
    "facet": ["area_name", "area_type", "variable", "year", "sex", "race", "data_type"],
    "refine.area_type": "County",
    "refine.year": "2020",
    "offset+limit": "10000"
}

response = requests.get(base_url, params=params, headers=headers).json()
response
print(json.dumps(response, indent=4, sort_keys=True))


# In[51]:


#put into .json file with proper formatting
data_list = [record['fields'] for record in response['records']]
with open('Resources/population-by-age-race-sex-linc.json', 'w') as json_file:
    json.dump(data_list, json_file)

#read json file
pop_ars = pd.read_json("Resources/population-by-age-race-sex-linc.json")
print(pop_ars.head())
print(len(pop_ars))


# In[52]:


from config import NC_osbm_key
base_url = "https://linc.osbm.nc.gov/api/records/1.0/search/?"
headers = {
    "Authorization": f"Apikey {NC_osbm_key}"
}
params = {
    "dataset": "social-and-human-services-linc",
    "q": "",
    "rows": 9000,
    "facet": ["area_name", "type", "year", "variable"],
    "refine.year": "2020",
    "offset+limit": "9000"
}

response = requests.get(base_url, params=params, headers=headers).json()
response
print(json.dumps(response, indent=4, sort_keys=True))


# In[53]:


#put into .json file with proper formatting
data_list = [record['fields'] for record in response['records']]
with open('Resources/social-and-human-services-linc.json', 'w') as json_file:
    json.dump(data_list, json_file)

#read json file
social_stats = pd.read_json("Resources/social-and-human-services-linc.json")
print(social_stats.head())
print(len(social_stats))

