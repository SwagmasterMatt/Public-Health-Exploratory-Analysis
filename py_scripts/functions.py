#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import numpy as np
from pathlib import Path


def Master_DF():
    # read CSV from Clean_Resources folder
    file = "Clean_Resources/Master_NC_Dataframe_2020.csv"
    # create dataframe
    Master_NC_Dataframe = pd.read_csv(file)
    # return dataframe
    return Master_NC_Dataframe

Master_NC_Dataframe = pd.DataFrame(Master_DF())


# In[94]:


columns = pd.DataFrame(Master_NC_Dataframe.columns)
#columns.to_clipboard(index=False, header=False)
column_list = columns[0].tolist()
len(column_list)


# In[95]:


"""
County
year
Per 1000: Health Care: Active Dentists
Per 1000: Health Care: Active Primary Care Physicians
Per 1000: Health Care: Beds in General Hospitals
Per 1000: Health Care: Deaths by Injury or Violence
Divorces
Per 1000: Health Care: General Hospital Discharges
Infant Deaths
Per 1000: Health Care: Low-Weight Births Under 2500 Grams
Marriages
Per 1000: Health Care: Midlevel Practitioners
Per 1000: Health Care: Nongeriatric Deaths
Per 1000: Health Care: Nursing Facility Beds
Per 1000: Health Care: Persons Served in Area Mental Health Programs
Per 1000: Health Care: Pregnancies for Females 15-19
Per 1000: Health Care: Pregnancies for Females of All Ages
Per 1000: Health Care: Registered Nurses
Per 1000: Health Care: Reported Abortions
Per 1000: Health Care: Resident Deaths
Per 1000: Health Care: Resident Live Births
Per 1000: Health Care: Total Active Physicians, Nonfederal, Non-resident-in-tr
Am. Indian Alaska Native Median Household Income
Am. Indian Alaska Native Per Capita Money Income (Census)
Am. Indian Alaska Native Persons in Poverty
Am. Indian Alaska Native Population for Whom Poverty Is Determined
Annual Wages by Place of Work
Average Annual Employment by Place of Work
Average Annual Wage per Worker
Black Median Household Income
Black Persons for Whom Poverty Status Is Determined
Black Persons in Poverty
Black Unemployment Rate (ACS)
Employed Females Age 16 Up
Employed Males Age 16 Up
Employment by Place of Residence
Estimated Median Family Income(HUD)
Families in Poverty
Families in Poverty with Female Householder
Families in Poverty with Related Children
Families in Poverty/Female Householder & Children
Per 1000: Income: Families with Income $10,000-14,999
Per 1000: Income:Families with Income $15,000-24,999
Per 1000: Income:Families with Income $25,000-49,999
Per 1000: Income:Families with Income $50,000 or More
Female Unemployment Rate (ACS)
Per 1000: Income:Females Age 16 Up in Labor Force
First Quarter Payroll by Place of Work
Hispanic Median Household Income
Hispanic Persons in Poverty
Hispanic Population for Whom Poverty is Determined
Labor Force by Place of Residence
Male Unemployment Rate (ACS)
Males Age 16 Up in Labor Force
Manufacturing Employment by Place of Work
Manufacturing Employment for Residents Age 16 Up
Mean Family Income
Median Family Income
Median Female Income
Median Household Income_x
Median Income
Median Male Income
Nonagric. Wage & Salary Employment by Place of Work
Nonmanuf. Employment for Residents Age 16 Up
Nonmanufacturing Employment by Place of Work
Per Capita Money Income (Census)
Percent  of White Persons in Poverty
Percent of Am. Indian Alaska Native Persons in Poverty
Percent of Black Persons in Poverty
Percent of Hispanic Persons in Poverty
Percent of Persons 65 Up in Poverty
Percent of Persons in Poverty
Percent of Related Children under 18 in Poverty
Percent of Related Children under 6 in Poverty
Persons 65 Up for Whom Poverty Status Is Determined
Persons 65 Up in Poverty
Persons for Whom Poverty Status Is Determined
Persons in Poverty
Related Children under 18 in Poverty
Related Children under 18-Poverty Status Determined
Related Children under 6 in Poverty
Related Children under 6-Poverty Status Determined
Unemployed Females Age 16 Up
Unemployed Males Age 16 Up
Unemployment Rate (ACS)
Unemployment Rate by Place of Residence (Percent)
Unemployment by Place of Residence
White Persons for Whom Poverty Status Is Determined
White Persons in Poverty
FIPS
Pct HS Educated
People (<High School)
National Rank (HS Education)
Median Household Income_y
National Rank (Income)
Percent Below Poverty
People (Below Poverty)
National Rank (Poverty)
Percent Unemployed
People (Unemployed)
National Rank (Unemployment)
Black Population
Population (Census/Estimate/Projection)
Population Density (Persons per Square Mile)
county longitude
county latitude
place_id
Bachelor's Degree or Higher Am. Indian Alaska Native Age 25 Up
Black Age 25 Up w/Elementary School Education or Less
College Enrollment
College Graduates Age 25 Up
Community College Enrollment
Elementary School Education or Less Age 25 Up
Enrollment in Home Schools
High School Enrollment
High School Graduates (incl. Equivalency) Am. Indian Alaska Native Age 25 Up
High School Graduates Age 25 Up
High School Graduates Black Age 25 Up
High School Graduates White Age 25 Up
Kindergarten and Elementary School Enrollment
Less Than 5 Years of Elementary School Age 25 Up
Less Than High School Diploma Am. Indian Alaska Native Age 25 Up
Nonpublic School Enrollment
Nursery School Enrollment
Preprimary or Kindergarten School Enrollment
Private College Enrollment
Public College Enrollment
Public High School Dropouts
Public High School Final Enrollment
Public High School Graduates
Public School Expenditures (000s)
Public School Expenditures - Federal (000s)
Public School Expenditures - Local (000s)
Public School Expenditures - State (000s)
Public School Final Average Daily Attendance
Public School Final Average Daily Membership
Public School Final Enrollment
Public School First Month Average Daily Membership
Public School First Month Membership
Public School Instructional Personnel
SAT Redesign Average ERW Score
SAT Redesign Average Math Score
SAT Redesign Total Average Score
Some College or Associate's Degree Am. Indian Alaska Native Age 25 Up
White Age 25 Up w/Elementary School Education or Less
Aged Recipients of Federally Administered SSI
Average Monthly Household Recipients of Food Stamps
Average Monthly Recipients of Food Stamps
Average Monthly Subsidized Children in Day Care
Children Under DSS Placement Responsibility
Disabled Medicare Enrollees with Hospital Coverage
Disabled Recipients of Federally Administered SSI
Licensed Capacity of Child Day Care Facilities
Licensed Child Day Care Facilities
Medicare Enrollees Age 65+ with Hosp/Med Coverage
Medicare Enrollees Age 65+ with Medical Coverage
Social Security Beneficiaries
Social Security Disabled Worker Beneficiaries
Social Security Retired Worker Beneficiaries
Substantiated Reports of Child Abuse
Substantiated Reports of Child Abuse and Neglect
Substantiated Reports of Child Neglect
Unduplicated Count of Medicaid Eligibles
Work First Recipients
death_per_1000_infant_death
"""


# In[96]:


#per 1000
data_categories = {
    'per_1000': {
        'Healthcare Personnel and Facilities': [
            'Active Dentists',
            'Active Primary Care Physicians',
            'Beds in General Hospitals',
            'General Hospital Discharges',
            'Midlevel Practitioners',
            'Nursing Facility Beds',
            'Persons Served in Area Mental Health Programs',
            'Registered Nurses',
            'Total Active Physicians, Nonfederal, Non-resident-in-tr'
        ],
        'Female_Other_Age': [
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
            'Female-Other-Population Age 85 and Over'
        ],
        'Female_White_Age': [
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
            'Female-White-Population Age 85 and Over'
        ],
        'Male_White_Age': [
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
        ],
        'Male_Other_Age': [
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
            'Male-Other-Population Age 85 and Over'
        ],
        'Birth and Death Statistics': [
            'Infant Deaths',
            'Low-Weight Births Under 2500 Grams',
            'Deaths by Injury or Violence',
            'Nongeriatric Deaths',
            'Resident Deaths',
            'Resident Live Births'
        ],
        'Life Events and Family Planning': [
            'Divorces',
            'Marriages',
            'Pregnancies for Females 15-19',
            'Pregnancies for Females of All Ages',
            'Reported Abortions',
            'Substantiated Reports of Child Abuse',
            'Substantiated Reports of Child Abuse and Neglect',
            'Substantiated Reports of Child Neglect'
        ],
        'Income and Wages': [
            'Am. Indian Alaska Native Per Capita Money Income (Census)',
            'Annual Wages by Place of Work',
            'Families with Income $10,000-14,999',
            'Families with Income $15,000-24,999',
            'Families with Income $25,000-49,999',
            'Families with Income $50,000 or More',
            'First Quarter Payroll by Place of Work',
            'Per Capita Money Income (Census)'
        ],
        'Employment and Unemployment': [
            'People (Unemployed)',
            'Employed Females Age 16 Up',
            'Employed Males Age 16 Up',
            'Employment by Place of Residence',
            'Females Age 16 Up in Labor Force',
            'Labor Force by Place of Residence',
            'Males Age 16 Up in Labor Force',
            'Manufacturing Employment by Place of Work',
            'Manufacturing Employment for Residents Age 16 Up',
            'Nonagric. Wage & Salary Employment by Place of Work',
            'Nonmanuf. Employment for Residents Age 16 Up',
            'Nonmanufacturing Employment by Place of Work',
            'Unemployed Females Age 16 Up',
            'Unemployed Males Age 16 Up',
            'Unemployment by Place of Residence'
        ],
        'Poverty and Welfare': [
            'Am. Indian Alaska Native Persons in Poverty',
            'Am. Indian Alaska Native Population for Whom Poverty Is Determined',
            'Black Persons for Whom Poverty Status Is Determined',
            'Black Persons in Poverty',
            'Black Population',
            'People (Below Poverty)',
            'Families in Poverty',
            'Families in Poverty with Female Householder',
            'Families in Poverty with Related Children',
            'Families in Poverty/Female Householder & Children',
            'Hispanic Persons in Poverty',
            'Hispanic Population for Whom Poverty is Determined',
            'Persons 65 Up for Whom Poverty Status Is Determined',
            'Persons 65 Up in Poverty',
            'Persons for Whom Poverty Status Is Determined',
            'Persons in Poverty',
            'Related Children under 18 in Poverty',
            'Related Children under 18-Poverty Status Determined',
            'Related Children under 6 in Poverty',
            'Related Children under 6-Poverty Status Determined',
            'White Persons for Whom Poverty Status Is Determined',
            'White Persons in Poverty'
        ],
        'Education': [
            'People (<High School)',
            'Bachelor\'s Degree or Higher Am. Indian Alaska Native Age 25 Up',
            'Black Age 25 Up w/Elementary School Education or Less',
            'College Enrollment',
            'College Graduates Age 25 Up',
            'Community College Enrollment',
            'Elementary School Education or Less Age 25 Up',
            'Enrollment in Home Schools',
            'High School Enrollment',
            'High School Graduates (incl. Equivalency) Am. Indian Alaska Native Age 25 Up',
            'High School Graduates Age 25 Up',
            'High School Graduates Black Age 25 Up',
            'High School Graduates White Age 25 Up',
            'Kindergarten and Elementary School Enrollment',
            'Less Than 5 Years of Elementary School Age 25 Up',
            'Less Than High School Diploma Am. Indian Alaska Native Age 25 Up',
            'Nonpublic School Enrollment',
            'Nursery School Enrollment',
            'Preprimary or Kindergarten School Enrollment',
            'Private College Enrollment',
            'Public College Enrollment',
            'Public High School Dropouts',
            'Public High School Final Enrollment',
            'Public High School Graduates',
            'Public School Expenditures (000s)',
            'Public School Expenditures - Federal (000s)',
            'Public School Expenditures - Local (000s)',
            'Public School Expenditures - State (000s)',
            'Public School Final Average Daily Attendance',
            'Public School Final Average Daily Membership',
            'Public School Final Enrollment',
            'Public School First Month Average Daily Membership',
            'Public School First Month Membership',
            'Public School Instructional Personnel',
            'Some College or Associate\'s Degree Am. Indian Alaska Native Age 25 Up',
            'White Age 25 Up w/Elementary School Education or Less'
        ],
        'Welfare and Social Security': [
            'Aged Recipients of Federally Administered SSI',
            'Average Monthly Household Recipients of Food Stamps',
            'Average Monthly Recipients of Food Stamps',
            'Average Monthly Subsidized Children in Day Care',
            'Children Under DSS Placement Responsibility',
            'Disabled Medicare Enrollees with Hospital Coverage',
            'Disabled Recipients of Federally Administered SSI',
            'Licensed Capacity of Child Day Care Facilities',
            'Licensed Child Day Care Facilities',
            'Unduplicated Count of Medicaid Eligibles',
            'Medicare Enrollees Age 65',
            'Medicare Enrollees Age 65+ with Hosp/Med Coverage',
            'Medicare Enrollees Age 65+ with Medical Coverage',
            'Social Security Beneficiaries',
            'Social Security Disabled Worker Beneficiaries',
            'Social Security Retired Worker Beneficiaries',
            'Work First Recipients'
        ]
    },
    'not_per_1000': {
        'Healthcare Personnel and Facilities': [],
        'Birth and Death Statistics': [],
        'Life Events and Family Planning': [],
        'Income and Wages': [
            'Am. Indian Alaska Native Median Household Income',
            'Average Annual Wage per Worker',
            'Estimated Median Family Income(HUD)',
            'Black Median Household Income',
            'Hispanic Median Household Income',
            'Mean Family Income',
            'Median Family Income',
            'Median Female Income',
            'Median Household Income_x',
            'Median Income',
            'Median Male Income',
            'National Rank (Income)'
        ],
        'Employment and Unemployment': [
            'Average Annual Employment by Place of Work',
            'Black Unemployment Rate (ACS)',
            'Female Unemployment Rate (ACS)',
            'Male Unemployment Rate (ACS)',
            'Unemployment Rate (ACS)',
            'Unemployment Rate by Place of Residence (Percent)',
            'Percent Unemployed',
            'National Rank (Unemployment)'
        ],
        'Poverty and Welfare': [
            'Percent of White Persons in Poverty',
            'Percent of Am. Indian Alaska Native Persons in Poverty',
            'Percent of Black Persons in Poverty',
            'Percent of Hispanic Persons in Poverty',
            'Percent of Persons 65 Up in Poverty',
            'Percent of Persons in Poverty',
            'Percent of Related Children under 18 in Poverty',
            'Percent of Related Children under 6 in Poverty',
            'Percent Below Poverty',
            'National Rank (Poverty)'
        ],
        'Education': [
            'Average SAT Math Score',
            'Average SAT Reading Score',
            'SAT Redesign Average ERW Score',
            'SAT Redesign Average Math Score',
            'SAT Redesign Total Average Score',
            'Pct HS Educated',
            'National Rank (HS Education)'
        ],
        'Geographic and Census Data': [
            'County',
            'year',
            'FIPS',
            'Population (Census/Estimate/Projection)',
            'Population Density (Persons per Square Mile)',
            'county longitude',
            'county latitude',
            'place_id'
        ],
        'Welfare and Social Security': [
            'Average Monthly Household Recipients of Food Stamps',
            'Average Monthly Recipients of Food Stamps'
        ]
    }
}

def find_dup_and_missing():
    # find columns that are not in the above dictionary and print them out
    found_columns = []
    missing_columns = []
    for column in column_list:
        found = False
        for category in data_categories['per_1000'].keys():
            if column in data_categories['per_1000'][category]:
                found = True
                found_columns.append(column)
                if found:
                    for category in data_categories['not_per_1000'].keys():
                        if column in data_categories['not_per_1000'][category]:
                            found_columns.append(column)
        if not found:
            for category in data_categories['not_per_1000'].keys():
                if column in data_categories['not_per_1000'][category]:
                    found = True

        if not found:
            missing_columns.append(column)





    print(pd.DataFrame(missing_columns))
    #count duplicates in found_columns
    print(pd.DataFrame(found_columns).duplicated().sum())
    #print dupplicates names
    print(pd.DataFrame(found_columns)[(pd.DataFrame(found_columns).duplicated()) == True])

def category_columns():
    per_1000_df = pd.DataFrame(data_categories['per_1000'].keys())
    not_per_1000_df = pd.DataFrame(data_categories['not_per_1000'].keys())
    Category_df = pd.concat([per_1000_df, not_per_1000_df], axis=1)
    Category_df.columns = ['per_1000', 'not_per_1000']
    return Category_df

Category_df = category_columns()

