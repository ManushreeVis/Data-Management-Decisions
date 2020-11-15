# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:48:40 2020

@author: manus_fabt4g4
"""


import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt


#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

data = pandas.read_csv('subfile.csv',low_memory=False,index_col=0)
data["S3AQ2A1"] = data["S3AQ2A1"].replace(" ",numpy.nan)

data["S3AQ2A1"] = pandas.to_numeric(data["S3AQ2A1"])
##recode values to missing values Nan
data["S3AQ2A1"] = data["S3AQ2A1"].replace(99,numpy.nan)

#CHECK321
data["CHECK321"] = data["CHECK321"].replace(" ",numpy.nan)
data["CHECK321"] = pandas.to_numeric(data["CHECK321"])
data["CHECK321"] = data["CHECK321"].replace(9,numpy.nan)

#S3AQ51
data["S3AQ51"] = data["S3AQ51"].replace(" ",numpy.nan)
data["S3AQ51"] = pandas.to_numeric(data["S3AQ51"])
data["S3AQ51"] = data["S3AQ51"].replace(99,numpy.nan)
#S3AQ10D
data["S3AQ10D"] = data["S3AQ10D"].replace(" ",0)
data["S3AQ10D"] = pandas.to_numeric(data["S3AQ10D"])
data["S3AQ10D"] = data["S3AQ10D"].replace(99,numpy.nan)

#S3AQ10GR
#here " " (Bl.)is replaced by 0, denoting that the symptom and/or duration criteria for lifetime nicotine
# dependence didn't meet
#-----------------------------------------------------------
data["S3AQ10GR"] = data["S3AQ10GR"].replace(" ",numpy.nan)
data["S3AQ10GR"] = pandas.to_numeric(data["S3AQ10GR"],errors='coerce')
data["S3AQ10GR"] = data["S3AQ10GR"].replace(99,numpy.nan)
#subset the original data
sub1 = data[['S3AQ2A1',"S3AQ51","CHECK321","S3AQ10GR"]].copy()
#rename columns to meaningful name
sub1 = sub1.rename(columns={'S3AQ2A1':'StartedSmokingAt',"S3AQ51":"SmokedEverydayAt","CHECK321":"SmokingStatus","S3AQ10GR":"RecentEpisode"})
#copy the subset and perform other operations
sub2 = sub1.copy()
sub2 = sub2.dropna()

#univariate histogram for quantitative variables
seaborn.distplot(sub2['StartedSmokingAt'],kde=False)
plt.xlabel="Age (in years)"
plt.title="Age when started to smoke"
desc1 = sub2['StartedSmokingAt'].describe()
print(desc1)
print(sub2['StartedSmokingAt'].mode())
#unimodal skewed right 10-20
seaborn.distplot(sub2['SmokedEverydayAt'],kde=False)
plt.xlabel="Age (in years)"
plt.title="Age when started to smoke regularly"
desc2 = sub2['SmokedEverydayAt'].describe()
print(desc2)
print(sub2['SmokedEverydayAt'].mode())
print(sub2['SmokedEverydayAt'].median())
#unimodal skewed right 15-25
#univariate bar graph for categorical variables 

sub2['SmokingStatus'] = sub2['SmokingStatus'].astype('category') 
seaborn.countplot(x="SmokingStatus",data=sub2)
plt.xlabel="1(yes) or 0(no) for active status in past 12 months"
plt.title=("1(yes) or 0(no) for active status in past 12 months")
desc3 = sub2['SmokingStatus'].describe()
print(desc3)
#unimodal highest peak at category 1.0

#scatter-plot Q->Q 
#startedsmokingeveryday recentepisode
scat1 = seaborn.regplot(x="SmokedEverydayAt", y="RecentEpisode", fit_reg=False, data=sub2)
plt.xlabel='Started Smoking Everyday at the age'
plt.ylabel='Recent Episode'
plt.title='Scatterplot for the Association Between Age Started Smoking Daily and Recent Episode'

#with the fitline
scat1_fit = seaborn.regplot(x="SmokedEverydayAt", y="RecentEpisode", fit_reg=True, data=sub2)
plt.xlabel='Started Smoking Everyday at the age'
plt.ylabel='Recent Episode'
plt.title='Scatterplot for the Association Between Age Started Smoking Daily and Recent Episode'

scat2 = seaborn.regplot(x="StartedSmokingAt", y="RecentEpisode", fit_reg=False, data=sub2)
plt.xlabel='Started Smoking  at the age'
plt.ylabel='Recent Episode'
plt.title='Scatterplot for the Association Between Age Started Smoking  and Recent Episode'

scat2_fit = seaborn.regplot(x="StartedSmokingAt", y="RecentEpisode", fit_reg=True, data=sub2)
plt.xlabel='Started Smoking  at the age'
plt.ylabel='Recent Episode'
plt.title='Scatterplot for the Association Between Age Started Smoking  and Recent Episode'

#C->Q
# bivariate bar graph C->Q
seaborn.catplot(x='SmokingStatus', y='RecentEpisode', data=sub2, kind="bar", ci=None)
plt.xlabel="Smoking Status"
plt.ylabel='Recent Episode'

#
#c11= sub2.groupby('SmokingStatus').size()
#print (c11)
sub3  =sub2.copy()
# quartile split (use qcut function & ask for 4 groups - gives you quartile split)
#print ('Started Smoking age - 10 categories')
#sub3['StartedSmokingAt']=pandas.qcut(sub3['StartedSmokingAt'], 10,duplicates='drop')
#c10 = sub3['StartedSmokingAt'].value_counts(sort=False, dropna=True)
#print(c10)
#
##seaborn.catplot(x='StartedSmokingAt', y='SmokingStatus', data=sub3,kind="bar",ci=None)
#fig , ax = plt.subplots()
#ax.bar(sub3['StartedSmokingAt'],sub3['SmokingStatus'])
scat4 = seaborn.regplot(x="StartedSmokingAt", y="SmokedEverydayAt", fit_reg=True, data=sub2)

