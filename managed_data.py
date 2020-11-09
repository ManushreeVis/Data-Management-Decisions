# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:44:10 2020

@author: manus_fabt4g4
"""


import numpy
import pandas
'''
       'S3AQ2A1':"AGE WHEN SMOKED FIRST FULL CIGARETTE",
       'CHECK321':"CIGARETTE SMOKING STATUS",
       'S3AQ51':"AGE STARTED SMOKING CIGARETTES EVERY DAY",
       'S3AQ10D':" AGE AT ONSET OF NICOTINE DEPENDENCE",
       'S3AQ10GR': " AGE WHEN ONLY/MOST RECENT EPISODE OF NICOTINE DEPENDENCE "
'''
data = pandas.read_csv('subfile.csv', low_memory=False)

##managing the missing data

#fornow.value_counts(sort=False, dropna=True)
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
data["S3AQ10GR"] = data["S3AQ10GR"].replace(" ",0)
data["S3AQ10GR"] = pandas.to_numeric(data["S3AQ10GR"])
data["S3AQ10GR"] = data["S3AQ10GR"].replace(99,numpy.nan)

#subset the original data
sub1 = data[['S3AQ2A1',"S3AQ51","CHECK321","S3AQ10GR"]].copy()
#rename columns to meaningful name
sub1 = sub1.rename(columns={'S3AQ2A1':'StartedSmokingAt',"S3AQ51":"SmokedEverydayAt","CHECK321":"SmokingStatus","S3AQ10GR":"RecentEpisode"})
#copy the subset and perform other operations
sub2 = sub1.copy()
#drop all the null values
sub2 = sub2.dropna()
#find mean and mode of the data columnwise to establih relation among them

#the average age at which person started smoking
ageSmokedFirst = sub2['StartedSmokingAt'].mode()
print(ageSmokedFirst)
print()
print('age at which average number of the people started smoking is ', ageSmokedFirst)
#the average age at which person started smoking everyday
smokingEveryday = sub2['SmokedEverydayAt'].mode()

smokingEveryday_mean = sub2['SmokedEverydayAt'].mean()
#print(smokingEveryday_mean)
print('age at which average number of the people started smoking EVERYDAY is ', smokingEveryday)
#the average smoking status of people
smokingStatus = sub2['SmokingStatus'].mode()
print('smoking Status :' ,smokingStatus)
print('Active smoker in past 12 months.')
print()
#if(smokingStatus==(1.0)):
#    
#    print('smoking Status :' ,smokingStatus)
#    print('Active smoker in past 12 months.')
#else:
#    print('smoking Status :' ,smokingStatus)
#    print('Smoked cigarettes prior to the last 12 months')

#replace 0's with nan in recent episode column
#as it does not help to determine the statistics
    #0, denoting that the symptom and/or duration criteria for lifetime nicotine
# dependence didn't meet

sub3 = sub2.copy()
sub3 = sub3['RecentEpisode'].replace(0,numpy.nan)
sub3 = sub3.dropna()
episodeFirst = sub3.mode()
#episodeFirst_mean = sub3.mean()
print('age at which experienced episode first ', episodeFirst)






