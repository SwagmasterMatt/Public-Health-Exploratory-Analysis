# Public Health Exploratory Analysis
This project was created for the UNC Data Analytics Bootcamp.
## Authors
- Matthew Ray (@SwagmasterMatt)
- Sam Lind (@SamLind11)
- Lori Girton (@ )
- Jeremy Magee (@ )

## Introduction

The goal of this project was to explore socio-economic factors which may correlate with and cause variations in infant mortality in North Carolina.  Using data collected from the NC Office of Budget Management API and the National Instutute of Health, we examined factors related to race, poverty, education, the presence of healthcare facilities and personnel, and public health to look for trends in NC's 100 counties.  The data was aggregated into a DataFrame, which was used to develop an array of data visualizations and implement machine learning algorithms.  

## Deliverables
- api_call.ipnyb
Description
- chi_tests.ipynb
Description
- data_collection.ipynb
Description
- data_exploration.ipynb
Description
- data_visualization.ipynb
Description
- functions.ipynb
Description

## Key Questions
1.  What factors correlate with infant mortality rates in North Carolina at the county level?
2.	How do changing socio-economic factors contribute to the differing rates of infant mortality between counties?
3.	What sub-factors of poverty are present consistently throughout socio-economic factors?
4.	What spurious correlations did we find in this analysis?

## Data Collection and Data Cleaning
The data for this analysis was collected from a combination of publicly available APIs and online databases.  The NC Office of State Budget and Management API provided data related to education rates, health facilities, and poverty for each county in North Carolina.  Additionally, we queried the National Institute of Health for further statistics on public health, education, population demographics, and per capita income by county.  Our Jupyter Notebook file (data_collection.ipynb) contains all API calls and reads in the NIH data from JSON files located in the Resources file.  These data were assembled into a master DataFrame for initial analysis.

One aspect of data cleaning was to determine what to do with the null data. For example, there were several counties that were missing infant mortality per 1000 data. Since this is an integral part of our analysis, we decided to add zero to the missing information. When comparing the top 5 and bottom 5 counties for number of infant deaths per 1000, we decided to write a DataFrame that ignored the zeros before determining the bottom 5 counties.

## Question 1: What factors correlate with infant mortality rates in North Carolina at the county level?

We found an article about a study by the US National Center for Health Statistics on Infant Mortality in the US (Ely & Driscoll, 2022). Among the examined trends, North Carolina was among the sixteen states with significantly higher than average infant mortality rates.

In order to explore the relationships which may correlate with infant mortality, the data first needed to be normalized by county population.  Many of the values collected from APIs and online databases were single population counts, and thus needed to be converted to per thousand county residents.  After these values were converted, a correlation heatmap was generated in order to identify strong correlations that existed in the data.

Figure 1: ![heatmap2](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/131621692/fee25f78-c81c-41dc-b0a9-58731a87dfc1)

Figure 2: ![heatmap1](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/131621692/6e5eeaec-e9fb-43d2-9722-53381e44e4ec)

The first two correlation heat maps (Figure 1 and Figure 2) examine the correlation between number of non-white women per 1000 residents and various statistics related to public health, including infant deaths and low weight births (<2500 grams.)  A similar plot was generated for white women per 1000 residents.  The first apparent trend is that the larger the population of young non-white women in a county, the higher the infant mortality rate (r-values ranging from 0.53 to 0.63).  Additionally, younger ages of non-white women show higher correlation values.  In contrast, the correlation between the proportion of white women per county and infant mortality was negative (ranging from -0.64 to -0.26), suggesting that the whiter the population of a county, the lower the infant mortality rates.

Given that race has virtually no causal relationship with medical outcomes outside of socio-economic influences, further heatmaps (see Appendix) were generated to investigate correlations between poverty statistics and infant death, as well as relationships between counts of health care facilities and personnel by county.


## Question 2: How do changing socio-economic factors contribute to the differing rates of infant mortality between counties?

## Question 3: What sub-factors of poverty are present consistently throughout socio-economic factors?

## Question 4: What spurious correlations did we find in this analysis?
