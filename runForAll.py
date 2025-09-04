# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:32:01 2025

@author: Svalm
"""
import os 
import pandas as pd
import matplotlib.pyplot as plt
#%%
os.chdir(r'C:\Users\Svalm\OneDrive - East Mercia Rivers Trust\GeneralEMRT\pythonForDominika')
from FunctionsForCitizenScience import graphsForCitizenScience
#%%
# set save to true
save=True


# where is the data stored
dataLocation = r"C:\Users\Svalm\OneDrive - East Mercia Rivers Trust\GeneralEMRT\pythonForDominika\Horncastle Citizen Science Data Sheet_03Sep2025.csv"
df = pd.read_csv(dataLocation)    


#%% get sites sorted 
sites = pd.unique(df.Site)
# drop sites of no use: nan, Test Site, Option 1
remove_items = ['Test Site', 'Option 1']
# option 1: list comprehension (clean + safe)
sites = [i for i in sites if i not in remove_items][1:]


#%%
# create folder for all years
outputLocation = r'C:\Users\Svalm\OneDrive - East Mercia Rivers Trust\GeneralEMRT\pythonForDominika\0925_CitizenScienceGraphs\AllDates'

# years
dateStart=('12/12/2000')
dateEnd=('12/12/2030')

# run code
for site in sites:
    graphsForCitizenScience(dataLocation, site, dateStart, dateEnd, outputLocation, save)
    plt.close('all')

#%%
# folder for oct 23-sept 24 yr1 
outputLocation = r'C:\Users\Svalm\OneDrive - East Mercia Rivers Trust\GeneralEMRT\pythonForDominika\0925_CitizenScienceGraphs\year1'

# years
dateStart=('01/10/2023')
dateEnd=('30/09/2024')

# run code
for site in sites:
    graphsForCitizenScience(dataLocation, site, dateStart, dateEnd, outputLocation, save)
    plt.close('all')


#%%
# folder for y2 oct 24-sept25
outputLocation = r'C:\Users\Svalm\OneDrive - East Mercia Rivers Trust\GeneralEMRT\pythonForDominika\0925_CitizenScienceGraphs\year2'

# years
dateStart=('01/10/2024')
dateEnd=('30/09/2025')

# run code
for site in sites:
    graphsForCitizenScience(dataLocation, site, dateStart, dateEnd, outputLocation, save)
    plt.close('all')
