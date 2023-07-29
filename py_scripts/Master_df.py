#!/usr/bin/env python
# coding: utf-8

# # Data Collection
# 
# The goal of this file is to create a Dataframe which contains metrics for each county in North Carolina.

# In[27]:


# Dependencies

# TODO Add dependencies
import pandas as pd
import json
from pathlib import Path


# In[41]:


#read in csvs and jsons into dataframes and print head

#vital-statistics-and-health-linc.json
all_health_osbm_df = pd.read_json("Resources/vital_stats_linc.json")
#filter for 2020
all_health_osbm_df = all_health_osbm_df[all_health_osbm_df["year"] == 2020]
#filter for area_type = "County"
all_health_osbm_df = all_health_osbm_df[all_health_osbm_df["area_type"] == "County"]
print(all_health_osbm_df.columns)
#clean up area_name values with errors
all_health_osbm_df["area_name"] = all_health_osbm_df["area_name"].str.replace("Mcdowell County", "McDowell County")
all_health_osbm_df["area_name"] = all_health_osbm_df["area_name"].str.replace("Davie  County", "Davie County")
all_health_osbm_df["area_name"] = all_health_osbm_df["area_name"].str.replace("Samson County", "Sampson County")

all_health_osbm_df = all_health_osbm_df.pivot_table(index=["area_name","year"], columns=["variable"], values="value")
#put back into a dataframe
all_health_osbm_df = pd.DataFrame(all_health_osbm_df.to_records())
#replace all NaN with 0
all_health_osbm_df = all_health_osbm_df.fillna(0)
print(all_health_osbm_df.columns)
#put into a csv
all_health_osbm_df.to_csv("Clean_Resources/all_health_osbm_2020.csv", index=False)


# In[29]:


#employment-and-income-linc.json
all_employment_osbm_df = pd.read_json("Resources/employment_income_stats_linc.json")
print(all_employment_osbm_df.columns)
#filter for 2020
all_employment_osbm_df = all_employment_osbm_df[all_employment_osbm_df["year"] == 2020]
#filter for area_type = "County"
all_employment_osbm_df = all_employment_osbm_df[all_employment_osbm_df["area_type"] == "County"]
#clean up area_name values with errors
all_employment_osbm_df["area_name"] = all_employment_osbm_df["area_name"].str.replace("Mcdowell County", "McDowell County")
all_employment_osbm_df["area_name"] = all_employment_osbm_df["area_name"].str.replace("Davie  County", "Davie County")
all_employment_osbm_df["area_name"] = all_employment_osbm_df["area_name"].str.replace("Samson County", "Sampson County")

all_employment_osbm_df = all_employment_osbm_df.pivot_table(index=["area_name","year"], columns=["variable"], values="value")
#put back into a dataframe
all_employment_osbm_df = pd.DataFrame(all_employment_osbm_df.to_records())
#replace all NaN with 0
all_employment_osbm_df = all_employment_osbm_df.fillna(0)
print(all_employment_osbm_df.columns)
#put into a csv
all_employment_osbm_df.to_csv("Clean_Resources/all_employment_osbm_2020.csv", index=False)


# In[30]:


#population-by-age-race-sex-linc.json
all_population_demog_df = pd.read_json("Resources/population-by-age-race-sex-linc.json")
print(all_population_demog_df.columns)
#filter for 2020
all_population_demog_df = all_population_demog_df[all_population_demog_df["year"] == 2020]
#filter for area_type = "County"
all_population_demog_df = all_population_demog_df[all_population_demog_df["area_type"] == "County"]

#clean up area_name values with errors
all_population_demog_df["area_name"] = all_population_demog_df["area_name"].str.replace("Mcdowell County", "McDowell County")
all_population_demog_df["area_name"] = all_population_demog_df["area_name"].str.replace("Davie  County", "Davie County")
all_population_demog_df["area_name"] = all_population_demog_df["area_name"].str.replace("Samson County", "Sampson County")

#sort by variable then race then sex then area_name
all_population_demog_df = all_population_demog_df.sort_values(by=["sex", "race", "variable", "area_name"])

#create dataframe grouping by area_name and year and sex and race
for i, row in all_population_demog_df.iterrows():
    col_name = f"{row['sex']}-{row['race']}-{row['variable']}"
    all_population_demog_df.loc[i, col_name] = row['value']


column_order = [
    'area_name',
    'year',
    # Female-Other
    'Female-Other-Population Age 0-4', 
    'Female-Other-Population Age 5', 
    'Female-Other-Population Age 6-9',
    'Female-Other-Population Age 10-12', 
    'Female-Other-Population Age 13', 
    'Female-Other-Population Age 14',
    'Female-Other-Population Age 15',
    'Female-Other-Population Age 16-17', 
    'Female-Other-Population Age 18', 
    'Female-Other-Population Age 19', 
    'Female-Other-Population Age 20-24', 
    'Female-Other-Population Age 25-29', 
    'Female-Other-Population Age 30-34',
    'Female-Other-Population Age 35-39',
    'Female-Other-Population Age 40-44',
    'Female-Other-Population Age 45-49',
    'Female-Other-Population Age 50-54',
    'Female-Other-Population Age 55-59',
    'Female-Other-Population Age 60-64',
    'Female-Other-Population Age 65-69',
    'Female-Other-Population Age 70-74',
    'Female-Other-Population Age 75-79',
    'Female-Other-Population Age 80-84',
    'Female-Other-Population Age 85 and Over',
    # Female-White
    'Female-White-Population Age 0-4', 
    'Female-White-Population Age 5', 
    'Female-White-Population Age 6-9',
    'Female-White-Population Age 10-12',
    'Female-White-Population Age 13', 
    'Female-White-Population Age 14',
    'Female-White-Population Age 15',
    'Female-White-Population Age 16-17', 
    'Female-White-Population Age 18', 
    'Female-White-Population Age 19', 
    'Female-White-Population Age 20-24', 
    'Female-White-Population Age 25-29', 
    'Female-White-Population Age 30-34',
    'Female-White-Population Age 35-39',
    'Female-White-Population Age 40-44',
    'Female-White-Population Age 45-49',
    'Female-White-Population Age 50-54',
    'Female-White-Population Age 55-59',
    'Female-White-Population Age 60-64',
    'Female-White-Population Age 65-69',
    'Female-White-Population Age 70-74',
    'Female-White-Population Age 75-79',
    'Female-White-Population Age 80-84',
    'Female-White-Population Age 85 and Over',
    # Male-Other
    'Male-Other-Population Age 0-4', 
    'Male-Other-Population Age 5', 
    'Male-Other-Population Age 6-9',
    'Male-Other-Population Age 10-12',
    'Male-Other-Population Age 13', 
    'Male-Other-Population Age 14',
    'Male-Other-Population Age 15',
    'Male-Other-Population Age 16-17', 
    'Male-Other-Population Age 18', 
    'Male-Other-Population Age 19', 
    'Male-Other-Population Age 20-24', 
    'Male-Other-Population Age 25-29', 
    'Male-Other-Population Age 30-34',
    'Male-Other-Population Age 35-39',
    'Male-Other-Population Age 40-44',
    'Male-Other-Population Age 45-49',
    'Male-Other-Population Age 50-54',
    'Male-Other-Population Age 55-59',
    'Male-Other-Population Age 60-64',
    'Male-Other-Population Age 65-69',
    'Male-Other-Population Age 70-74',
    'Male-Other-Population Age 75-79',
    'Male-Other-Population Age 80-84',
    'Male-Other-Population Age 85 and Over',
    # Male-White
    'Male-White-Population Age 0-4', 
    'Male-White-Population Age 5', 
    'Male-White-Population Age 6-9',
    'Male-White-Population Age 10-12',
    'Male-White-Population Age 13', 
    'Male-White-Population Age 14',
    'Male-White-Population Age 15',
    'Male-White-Population Age 16-17', 
    'Male-White-Population Age 18', 
    'Male-White-Population Age 19', 
    'Male-White-Population Age 20-24', 
    'Male-White-Population Age 25-29', 
    'Male-White-Population Age 30-34',
    'Male-White-Population Age 35-39',
    'Male-White-Population Age 40-44',
    'Male-White-Population Age 45-49',
    'Male-White-Population Age 50-54',
    'Male-White-Population Age 55-59',
    'Male-White-Population Age 60-64',
    'Male-White-Population Age 65-69',
    'Male-White-Population Age 70-74',
    'Male-White-Population Age 75-79',
    'Male-White-Population Age 80-84',
    'Male-White-Population Age 85 and Over'
]

all_population_demog_df = all_population_demog_df[column_order]

print(all_population_demog_df.columns)
#collapse all rows by area_name and year
all_population_demog_df = all_population_demog_df.groupby(["area_name","year"]).sum()
#alphabetically sort columns after area_name and year

#reset index
all_population_demog_df = all_population_demog_df.reset_index()



"""
------------------BACK UP CODE
all_population_demog_df = all_population_demog_df.pivot_table(index=["area_name","year"], columns=["variable"], values="value")
#put back into a dataframe
all_population_demog_df = pd.DataFrame(all_population_demog_df.to_records())
#replace all NaN with 0
all_population_demog_df = all_population_demog_df.fillna(0)
print(all_population_demog_df.columns)
"""
#put into a csv
all_population_demog_df.to_csv("Clean_Resources/all_population_demog_2020.csv", index=False)



# In[31]:


#pop_migration_linc.json
all_population_counts_df = pd.read_json("Resources/pop_migration_linc.json")
print(all_population_counts_df.columns)

#filter for area type =  "County"
all_population_counts_df = all_population_counts_df[all_population_counts_df["area_type"] == "County"]
#filter data type to "Count"
all_population_counts_df = all_population_counts_df[all_population_counts_df["data_type"] == "Count"]
#clean up area_name column
all_population_counts_df["area_name"] = all_population_counts_df["area_name"].str.replace("Mcdowell County", "McDowell County")
all_population_counts_df["area_name"] = all_population_counts_df["area_name"].str.replace("Davie  County", "Davie County")
all_population_counts_df["area_name"] = all_population_counts_df["area_name"].str.replace("Samson County", "Sampson County")

all_population_counts_df = all_population_counts_df.pivot_table(index=["area_name", "year"], columns=["variable"], values="value")
#put back into a dataframe
all_population_counts_df = pd.DataFrame(all_population_counts_df.to_records())
#replace all NaN with 0
all_population_counts_df = all_population_counts_df.fillna(0)
print(all_population_counts_df.columns)
#put into a csv
all_population_counts_df.to_csv("Clean_Resources/all_population_counts_2020.csv", index=False)


# In[32]:


#NIH_high_school_ed.csv
#skip the first 5 rows of the csv

all_high_school_ed_df = pd.read_csv("Resources/NIH_high_school_ed.csv", skiprows=5)
#remove the last 5 rows
all_high_school_ed_df = all_high_school_ed_df[:-5]
print(all_high_school_ed_df.columns)
#remove United States and North Carolina rows
all_high_school_ed_df = all_high_school_ed_df[all_high_school_ed_df["County"] != "United States"]
all_high_school_ed_df = all_high_school_ed_df[all_high_school_ed_df["County"] != "North Carolina"]
#sort by county
all_high_school_ed_df = all_high_school_ed_df.sort_values(by=["County"])
#reset index
all_high_school_ed_df = all_high_school_ed_df.reset_index(drop=True)
#rename columns
all_high_school_ed_df = all_high_school_ed_df.rename(columns={"County": "area_name","Value (Percent)": "Pct HS Educated", "People(Education: Less Than High School)": "People (<High School)", "Rank within US (of 3142 counties)": "National Rank (HS Education)", " FIPS": "FIPS"})
all_high_school_ed_df["year"] = 2020
all_high_school_ed_df = all_high_school_ed_df[["area_name", "year", "FIPS", "Pct HS Educated", "People (<High School)", "National Rank (HS Education)"]]
print(all_high_school_ed_df.head())
print(all_high_school_ed_df["area_name"])
#put into a csv
all_high_school_ed_df.to_csv("Clean_Resources/all_high_school_ed_2020.csv", index=False)


# In[33]:


#NIH_median_income.csv
#skip the first 4 rows of the csv
all_median_income_df = pd.read_csv("Resources/NIH_median_income.csv", skiprows=4)
print(all_median_income_df.columns)
#remove the last 5 rows
all_median_income_df = all_median_income_df[:-6]
#remove United States and North Carolina rows
all_median_income_df = all_median_income_df[all_median_income_df["County"] != "United States"]
all_median_income_df = all_median_income_df[all_median_income_df["County"] != "North Carolina"]
#sort by county
all_median_income_df = all_median_income_df.sort_values(by=["County"])

#reset index
all_median_income_df = all_median_income_df.reset_index(drop=True)
all_median_income_df.rename(columns={"County": "area_name"," FIPS": "FIPS", "Value (Dollars)": "Median Household Income", "Rank within US (of 3141 counties)": "National Rank (Income)"}, inplace=True)
all_median_income_df["year"] = 2020
all_median_income_df = all_median_income_df[["area_name", "year", "FIPS", "Median Household Income", "National Rank (Income)"]]
print(all_median_income_df.head())
print(all_median_income_df["area_name"])
#put into a csv
all_median_income_df.to_csv("Clean_Resources/all_median_income_2020.csv", index=False)


# In[34]:


#NIH_persons_below_poverty.csv
#skip the first 4 rows of the csv
all_persons_below_poverty_df = pd.read_csv("Resources/NIH_persons_below_poverty.csv", skiprows=4)
#remove the last 5 rows
print(all_persons_below_poverty_df.columns)
all_persons_below_poverty_df = all_persons_below_poverty_df[:-5]
#remove United States and North Carolina rows
all_persons_below_poverty_df = all_persons_below_poverty_df[all_persons_below_poverty_df["County"] != "United States"]
all_persons_below_poverty_df = all_persons_below_poverty_df[all_persons_below_poverty_df["County"] != "North Carolina"]
#sort by county
all_persons_below_poverty_df = all_persons_below_poverty_df.sort_values(by=["County"])
#reset index
all_persons_below_poverty_df = all_persons_below_poverty_df.reset_index(drop=True)
all_persons_below_poverty_df.rename(columns={"County": "area_name"," FIPS": "FIPS", "Value (Percent)": "Percent Below Poverty", "Rank within US (of 3142 counties)": "National Rank (Poverty)"}, inplace=True)
all_persons_below_poverty_df["year"] = 2020
all_persons_below_poverty_df = all_persons_below_poverty_df[["area_name", "year", "FIPS", "Percent Below Poverty", "People (Below Poverty)","National Rank (Poverty)"]]
print(all_persons_below_poverty_df.head())
print(all_persons_below_poverty_df["area_name"])
#put into a csv
all_persons_below_poverty_df.to_csv("Clean_Resources/all_persons_below_poverty_2020.csv", index=False)


# In[35]:


#NIH_persons_unemployed.csv
#skip the first 4 rows of the csv
all_persons_unemployed_df = pd.read_csv("Resources/NIH_persons_unemployed.csv", skiprows=4)
print(all_persons_unemployed_df.columns)
#remove the last 5 rows
all_persons_unemployed_df = all_persons_unemployed_df[:-5]
#remove United States and North Carolina rows
all_persons_unemployed_df = all_persons_unemployed_df[all_persons_unemployed_df["County"] != "United States"]
all_persons_unemployed_df = all_persons_unemployed_df[all_persons_unemployed_df["County"] != "North Carolina"]
#sort by county
all_persons_unemployed_df = all_persons_unemployed_df.sort_values(by=["County"])
#reset index
all_persons_unemployed_df = all_persons_unemployed_df.reset_index(drop=True)
all_persons_unemployed_df.rename(columns={"County": "area_name"," FIPS": "FIPS", "Value (Percent)": "Percent Unemployed", "Rank within US (of 3142 counties)": "National Rank (Unemployment)"}, inplace=True)
all_persons_unemployed_df["year"] = 2020
all_persons_unemployed_df = all_persons_unemployed_df[["area_name", "year", "FIPS", "Percent Unemployed", "People (Unemployed)","National Rank (Unemployment)"]]
print(all_persons_unemployed_df.head())
print(all_persons_unemployed_df["area_name"])
#put into a csv
all_persons_unemployed_df.to_csv("Clean_Resources/all_persons_unemployed_2020.csv", index=False)


# In[36]:


#geoapify_counties json file

# Load the json file
with open("Resources/geoapify_counties.json") as f:
    data = json.load(f)

# Define the record path
record_path = ['features', 'properties']

# Extract the nested data into a DataFrame
df_list = [pd.json_normalize(feature) for feature in data['features']]

# Concatenate all the dataframes in the list into a single dataframe
counties_geoapify_df = pd.concat(df_list, ignore_index=True)
columns = [
    'properties.name',
    'properties.lon',
    'properties.lat',
    'properties.place_id',
    'properties.datasource.raw.nist:fips_code'
    ]
counties_geoapify_df = counties_geoapify_df[columns]
counties_geoapify_df = counties_geoapify_df.rename(columns={'properties.name': 'area_name', 'properties.lon': 'county longitude', 'properties.lat': 'county latitude', 'properties.place_id': 'place_id', 'properties.datasource.raw.nist:fips_code': 'FIPS'})
print(counties_geoapify_df.columns)
#to csv
counties_geoapify_df.to_csv('Clean_Resources/geoapify_counties.csv', index=False)




# In[37]:


#education_stats_linc.json
all_education_osbm_df = pd.read_json("Resources/education_stats_linc.json")
#filter for 2020
all_education_osbm_df = all_education_osbm_df[all_education_osbm_df["year"] == 2020]
#filter for area_type = "County"
all_education_osbm_df = all_education_osbm_df[all_education_osbm_df["area_type"] == "County"]
print(all_education_osbm_df.columns)
#clean up area_name values with errors
all_education_osbm_df["area_name"] = all_education_osbm_df["area_name"].str.replace("Mcdowell County", "McDowell County")
all_education_osbm_df["area_name"] = all_education_osbm_df["area_name"].str.replace("Davie  County", "Davie County")
all_education_osbm_df["area_name"] = all_education_osbm_df["area_name"].str.replace("Samson County", "Sampson County")

all_education_osbm_df = all_education_osbm_df.pivot_table(index=["area_name","year"], columns=["variable"], values="value")
#put back into a dataframe
all_education_osbm_df = pd.DataFrame(all_education_osbm_df.to_records())
#replace all NaN with 0
all_education_osbm_df = all_education_osbm_df.fillna(0)
print(all_education_osbm_df.columns)
#put into a csv
all_education_osbm_df.to_csv("Clean_Resources/all_education_osbm_2020.csv", index=False)


# In[38]:


#education_stats_linc.json
all_social_and_human_linc_df = pd.read_json("Resources/social-and-human-services-linc.json")
#filter for 2020
all_social_and_human_linc_df = all_social_and_human_linc_df[all_social_and_human_linc_df["year"] == 2020]
#filter for area_type = "County"
print(all_social_and_human_linc_df.columns)
#clean up area_name values with errors
all_social_and_human_linc_df["area_name"] = all_social_and_human_linc_df["area_name"].str.replace("Mcdowell County", "McDowell County")
all_social_and_human_linc_df["area_name"] = all_social_and_human_linc_df["area_name"].str.replace("Davie  County", "Davie County")
all_social_and_human_linc_df["area_name"] = all_social_and_human_linc_df["area_name"].str.replace("Samson County", "Sampson County")

all_social_and_human_linc_df = all_social_and_human_linc_df.pivot_table(index=["area_name","year"], columns=["variable"], values="value")
#put back into a dataframe
all_social_and_human_linc_df = pd.DataFrame(all_social_and_human_linc_df.to_records())
#replace all NaN with 0
all_social_and_human_linc_df = all_social_and_human_linc_df.fillna(0)
print(all_social_and_human_linc_df.columns)
#put into a csv
all_social_and_human_linc_df.to_csv("Clean_Resources/all_social_and_human_osbm_2020.csv", index=False)


# In[39]:


#Join all of the data frames by county and year
#merge all_health_osbm_df and all_employment_osbm_df
all_health_employment_df = pd.merge(all_health_osbm_df, all_employment_osbm_df, on=["area_name", "year"], how="outer")
#merge all_health_employment_df and all_population_demog_df
all_health_employment_demog_df = pd.merge(all_health_employment_df, all_population_demog_df, on=["area_name", "year"], how="outer")
#merge all_health_employment_demog_df and all_high_school_ed_df
all_health_employment_demog_ed_df = pd.merge(all_health_employment_demog_df, all_high_school_ed_df, on=["area_name", "year"], how="outer")
#merge all_health_employment_demog_ed_df and all_median_income_df
all_health_employment_demog_ed_income_df = pd.merge(all_health_employment_demog_ed_df, all_median_income_df, on=["area_name", "year", "FIPS"], how="outer")
#merge all_health_employment_demog_ed_income_df and all_persons_below_poverty_df
all_health_employment_demog_ed_income_poverty_df = pd.merge(all_health_employment_demog_ed_income_df, all_persons_below_poverty_df, on=["area_name", "year", "FIPS"], how="outer")
#merge all_health_employment_demog_ed_income_poverty_df and all_persons_unemployed_df
all_health_employment_demog_ed_income_poverty_unemployed_df = pd.merge(all_health_employment_demog_ed_income_poverty_df, all_persons_unemployed_df, on=["area_name", "year", "FIPS"], how="outer")
#merge all_health_employment_demog_ed_income_poverty_unemployed_df and all_population_counts_df
all_health_employment_demog_ed_income_poverty_unemployed_pop_df = pd.merge(all_health_employment_demog_ed_income_poverty_unemployed_df, all_population_counts_df, on=["area_name", "year"], how="outer")
#merge all_health_employment_demog_ed_income_poverty_unemployed_pop_df and counties_geoapify_df
all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_df = pd.merge(all_health_employment_demog_ed_income_poverty_unemployed_pop_df, counties_geoapify_df, on=["area_name", "FIPS"], how="outer")
#merge all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_df and all_education_osbm_df
all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_ed_df = pd.merge(all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_df, all_education_osbm_df, on=["area_name", "year"], how="outer")
#merge all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_ed_df and all_social_and_human_linc_df
all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_ed_social_df = pd.merge(all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_ed_df, all_social_and_human_linc_df, on=["area_name", "year"], how="outer")
#rename Master Dataframe
Master_NC_Dataframe = all_health_employment_demog_ed_income_poverty_unemployed_pop_geo_ed_social_df.rename(columns={"area_name": "County"})
#create death per 1000 infant death column
Master_NC_Dataframe['death_per_1000_infant_death'] = Master_NC_Dataframe['Infant Deaths'] / Master_NC_Dataframe['Population (Census/Estimate/Projection)'] * 1000
print(len(Master_NC_Dataframe))
#put into a csv
Master_NC_Dataframe.to_csv("Clean_Resources/Master_NC_Dataframe_2020.csv", index=False)

