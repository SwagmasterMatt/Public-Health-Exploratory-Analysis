# Public Health Exploratory Analysis
This project was created for the UNC Data Analytics Bootcamp.

## Authors
- Matthew Ray ([@SwagmasterMatt](https://github.com/SwagmasterMatt))
- Sam Lind ([@SamLind11](https://github.com/SamLind11))
- Lori Girton ([@LoriGirton](https://github.com/lorigirton))
- Jeremy Magee ([@JpMageeGitHub](https://github.com/JpMageeGitHub))

## Introduction

The goal of this project was to explore socio-economic factors which may correlate with and explain variations in infant mortality in North Carolina.  Using data collected from the NC Office of Budget Management API and the National Institute of Health, we examined factors related to race, poverty, education, the presence of healthcare facilities and personnel, and public health to look for trends in NC's 100 counties.  The data was aggregated into a DataFrame, which was used to develop an array of data visualizations and implement machine learning algorithms.  

## Key Questions
We set out to collect data and perform analysis which would answer the following equations:

1.  What factors correlate with infant mortality rates in North Carolina at the county level?
2.	How do changing socio-economic factors contribute to the differing rates of infant mortality between counties?
3.	What sub-factors of poverty are present consistently throughout socio-economic factors?

## Data Collection and Data Cleaning
The data for this analysis was collected from a combination of publicly available APIs and online databases.  The NC Office of State Budget and Management API provided data related to education rates, health facilities, and poverty for each county in North Carolina.  Additionally, we queried the National Institute of Health for further statistics on public health, education, population demographics, and per capita income by county.  Our Jupyter Notebook file (data_collection.ipynb) contains all API calls and reads in the NIH data from JSON files located in the Resources file.  These data were assembled into a master DataFrame for initial analysis.

One aspect of data cleaning was to determine what to do with the null data. For example, there were several counties that were missing infant mortality per 1000 data. Since this is an integral part of our analysis, we decided to add zero to the missing information. When comparing the top 5 and bottom 5 counties for number of infant deaths per 1000, we decided to write a DataFrame that ignored the zeros before determining the bottom 5 counties.

## Question 1: What factors correlate with infant mortality rates in North Carolina at the county level?

We found an article about a study by the US National Center for Health Statistics on Infant Mortality in the US (Ely & Driscoll, 2022). Among the trends examined, North Carolina was among the sixteen states with significantly higher than average infant mortality rates.

In order to explore the relationships which may correlate with infant mortality, the data first needed to be normalized by county population.  Many of the values collected from APIs and online databases were single population counts, and thus needed to be converted to per thousand county residents.  After these values were converted, a correlation heatmap was generated in order to identify strong correlations that existed in the data.

Figure 1: ![heatmap2](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/131621692/fee25f78-c81c-41dc-b0a9-58731a87dfc1)

Figure 2: ![heatmap1](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/131621692/6e5eeaec-e9fb-43d2-9722-53381e44e4ec)

The first two correlation heat maps (Figure 1 and Figure 2) examine the correlation between number of non-white women per 1000 residents and various statistics related to public health, including infant deaths and low weight births (<2500 grams.)  A similar plot was generated for white women per 1000 residents.  The first apparent trend is that the larger the population of young non-white women in a county, the higher the infant mortality rate (r-values ranging from 0.53 to 0.63).  Additionally, younger ages of non-white women show higher correlation values.  In contrast, the correlation between the proportion of white women per county and infant mortality was negative (ranging from -0.64 to -0.26), suggesting that the whiter the population of a county, the lower the infant mortality rates.

Given that race has virtually no causal relationship with medical outcomes outside of socio-economic influences, further heatmaps (Figure 3 and Figure 4) were generated to investigate correlations between poverty statistics and infant death, as well as relationships between counts of health care facilities and personnel by county.


## Question 2: How do changing socio-economic factors contribute to the differing rates of infant mortality between counties?

Figure 3: ![heatmap3](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/131621692/ba8b2abc-109a-47c1-aabf-49a42de47d42)

Figure 4: ![heatmap4](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/131621692/e655cfcc-cf0f-4ca9-9931-aabc9235afaa)

The correlation heatmap comparing poverty statistics and infant mortality (see Figure 3) show several possible explanations for why infant mortality may be higher in counties with higher non-white populations.  We can note that higher proportions of “People (Below Poverty)” and “Families in Poverty” correlate with higher infant mortality rates (r-values of 0.54 and 0.60 respectively).  We also see that “Black Population” is correlated with “People (Below Poverty)” and “Families in Poverty” (r-values of 0.57 and 0.59 respectively).  This suggests that poverty rates serve as better explanatory variables for infant mortality than race alone.

We also wondered whether counties in North Carolina with higher proportions of non-white women had differences in numbers of healthcare facilities and personnel.  The heatmap in Figure 4 suggests that variables such as “Beds in General Hospitals”, “Active Primary Care Physicians”, and “Registered Nurses” were not strongly correlated with populations of non-white women.  We thus conclude that these variables do not sufficiently explain differences in infant mortality between white and non-white women.

## Question 3: What sub-factors of poverty are present consistently throughout socio-economic factors?

"Families with a female head of house" (e.g. Single-Parent) was the most consistent sub-factor throughout our measured socioeconomic data. Within that grouping, those families with a Black female heads of house were more likely to experience an infant death than other racial groups.  Furthermore, the likelihood of a person in poverty being black (p = 0.341) was twice as likely as them being white (p = 0.17), despite the populations being in a ratio of White to Black women of 1.91:1. Other sub-factors that follow logically are the highest finished level of education, and level of income. The correlation of these factors was negative, as an increase in the highest level of education tends to reduce the level of poverty. This is clearly the case with level of income.

![Correlation 1](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/84f90e6f-dbee-4da0-b6a7-f17d36e7221e)
![Correlation 2](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/d3094610-fda3-4cf6-a4f6-e9c2b0189929)
![Correlation 5](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/d4266c1a-6f9f-487a-9d3d-6c7b8874d62c)
![Correlation 4](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/141272b9-c6d9-4951-b6bc-7bd4c6845b53)
![Correlation 3](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/666f4c82-a5d9-46e0-996f-062e58267a1a)
![Correlation 6](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/ee424cb8-d729-46d3-820e-15b3a120a713)

There was an abnormally high correlation with black persons in poverty with Black Age 25 and Up w/ Elementary School Education or Less

![Correlation 7](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/5e26673b-27fb-4765-83d3-9d780dd8bb4d)

Additionally, there was an interesting correlation between determined white poverty vs determined black poverty. The relationship suggested an inverse relationship - possibly suggesting geographic dispersion at the county level of race when races are in poverty.

![Correlation 8](https://github.com/SwagmasterMatt/Public-Health-Exploratory-Analysis/assets/133460903/43b9e6ef-548d-4035-a513-496e5182fa1f)

## Summary and Conclusions

North Carolina counties display variation in rates of infant mortality along lines of race.  However, we found that poverty rates serve as better indicators of infant mortality rates between counties.  In fact, as in many places in the United States, poverty afflicts black North Carolinians at much higher rates than it does white North Carolinians.  In our analysis, we found that other subfactors of poverty such as rates of high school graduation and numbers of households headed by women also pointed to higher rates of infant mortality.  

In further studies, we may look for additional data which predicts rates of poverty, education, and public health outcomes.  We found that the rate of Mid-level Health Practitioners in a county served as a good predictor of important factors such as poverty and infant mortality.  However, given that many other rates of healthcare personnel did not strongly correlate with infant mortality, this correlation would require further analysis to investigate its relevance.

## Limitations

The analysis in this document is primarily limited by the nature of the data collected.  The data collected from the North Carolina OSBM and the NIH were primarily counts provided for each county.  However, these counts, including those for infant mortality, were not broken down along lines of race or any socio-economic status.  We are therefore limited to analyzing relationships between these counts, and conclusions drawn would have major caveats, without the acquisition of more granular data. Such data is necessary to more carefully examine how socio-economic factors might influence infant mortality.

## Resources and References

Ely, Danielle M. & Driscoll, Anne K. (2022). Infant Mortality in the United States, 2020: Data From the Period Linked Birth/Infant Death File. National Vital Statistics Reports,  Volume 71, Number 5. Retrieved from https://www.cdc.gov/nchs/data/nvsr/nvsr71/nvsr71-05.pdf.

HDPulse: An Ecosystem of Minority Health and Health Disparities Resources. National Institute on Minority Health and Health Disparities. Created 7/25/2023. Available from https://hdpulse.nimhd.nih.gov

NC OSBM. (2023). API Console. Retrieved 7/27/2023, from https://linc.osbm.nc.gov/api/v2/console1.


