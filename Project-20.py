# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/cholera-data.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project-20 : Country wise Number of reported deaths from cholera");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

country = df.groupby(['Location'])[['Period']].count()
print("---------------------------------")
print("\tAvailable country names : ")
print("-------------------------------")
print(country)
print("-------------------------------")
count = 0
for row in range(len(country)): 
        count = count+1
print("total no. of country = ",count)        
print("-----------------------------\n")


# Question - D : Available years data for which data is available

years = df.groupby(['Period'])[['Location']].count()
print("---------------------------------")
print("\tAvailable years data : ")
print("-------------------------------")
print(years)
print("-------------------------------")
count = 0
for row in range(len(years)): 
        count = count+1
print("total no. of years = ",count)        
print("-----------------------------\n")


# Question - 01 : Afghanistan

Afghanistan = df[df.Location == 'Afghanistan']
print(Afghanistan[1:])
                                                                  
# Question - 02 : Algeria  

Algeria  = df[df.Location == 'Algeria']
print(Algeria[1:])                                                                         
                                                                                                                                                                                                                           
# Question - 03 : Argentina 

Argentina  = df[df.Location == 'Argentina']
print(Argentina[1:])                                  
                                                                                                      
# Question - 04 : Armenia 

Armenia = df[df.Location == 'Armenia']
print(Armenia[1:])

# Question - 05 : Bangladesh

Bangladesh = df[df.Location == 'Bangladesh']
print(Bangladesh[1:])

# Question - 06 : Central African Republic

Central_African_Republic = df[df.Location == 'Central African Republic']
print(Central_African_Republic[1:])

# Question - 07 : Chad

Chad = df[df.Location == 'Chad']
print(Chad[1:])

# Question - 08 : China

China = df[df.Location == 'China']
print(China[1:])

# Question - 09 : India

India = df[df.Location == 'India']
print(India[1:])

# Question - 10 : Indonesia

Indonesia = df[df.Location == 'Indonesia']
print(Indonesia[1:])

# Question - 11 : Thailand

Thailand = df[df.Location == 'Thailand']
print(Thailand[1:])

# Question - 12 : United Arab Emirates

UAE = df[df.Location == 'United Arab Emirates']
print(UAE[1:])
