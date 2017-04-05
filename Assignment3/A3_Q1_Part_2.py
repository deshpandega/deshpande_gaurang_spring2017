
# coding: utf-8

# # Q1_Part_Two
# 
# #### NYC Vehicle collision analysis
# #### For each borough, find distribution of each collision scale 

# In[1]:

# Import statements
from pandas import Series, DataFrame
import pandas as pd, numpy as np, os
from numpy import nan as NA


# In[2]:

# Take relative path for data
current_dir = os.path.dirname('__file__')
data_dir = os.path.join(current_dir, 'Data')
filename = 'vehicle_collisions.csv'

# Generate the file path by joining the directory path and file name for input csv file
file_path = os.path.join(data_dir, filename)


# In[3]:

# Read csv file using pd.read_csv
vehicle_df = pd.read_csv(file_path,sep=',')


# In[4]:

# Remove unwanted columns
vehicle_df = vehicle_df.drop(['UNIQUE KEY','DATE','TIME','ZIP CODE','LATITUDE','LONGITUDE','LOCATION','ON STREET NAME','CROSS STREET NAME','OFF STREET NAME','PERSONS INJURED','PERSONS KILLED','PEDESTRIANS INJURED','PEDESTRIANS KILLED','CYCLISTS INJURED','CYCLISTS KILLED','MOTORISTS INJURED','MOTORISTS KILLED','VEHICLE 1 FACTOR','VEHICLE 2 FACTOR','VEHICLE 3 FACTOR','VEHICLE 4 FACTOR','VEHICLE 5 FACTOR'], axis = 1)


# In[5]:

# Split dataframe into 2 different data frames to handle the NaN values differently

# Fill in NYC as NaN value in Borough
borough_df = vehicle_df.drop(['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'], axis = 1)
borough_df.fillna('NYC', inplace=True)


# In[6]:

# Leave values as NaN in vehicles involved
vehicles_involved_df = vehicle_df.drop(['BOROUGH'], axis = 1)

# Count the number of behicles involved for each index
vehicles_involved_df = vehicles_involved_df.count(axis=1)


# In[7]:

# Combine the data frame
vehicle_df = pd.concat([borough_df, vehicles_involved_df], axis=1)


# In[8]:

# Rename the column containing number of vehicles involved as COUNT 
vehicle_df.columns.values[1]='COUNT'
vehicle_df.head()


# In[9]:

# Generate dataframe to get values for QUEENS borough and number of vehicles involved
QUEENS_DF = DataFrame({})
QUEENS_DF['ONE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='QUEENS')&(vehicle_df['COUNT']==1)].count()
QUEENS_DF['TWO_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='QUEENS')&(vehicle_df['COUNT']==2)].count()
QUEENS_DF['THREE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='QUEENS')&(vehicle_df['COUNT']==3)].count()
QUEENS_DF['MORE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='QUEENS')&((vehicle_df['COUNT']>3)|(vehicle_df['COUNT']==0))].count()

# Cleaning the data frame and renaming 
QUEENS_DF.index.values[1]='QUEENS'
QUEENS_DF = QUEENS_DF.drop('BOROUGH')


# In[10]:

# Generate dataframe to get values for BRONX borough and number of vehicles involved
BRONX_DF = DataFrame({})
BRONX_DF['ONE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BRONX')&(vehicle_df['COUNT']==1)].count()
BRONX_DF['TWO_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BRONX')&(vehicle_df['COUNT']==2)].count()
BRONX_DF['THREE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BRONX')&(vehicle_df['COUNT']==3)].count()
BRONX_DF['MORE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BRONX')&((vehicle_df['COUNT']>3)|(vehicle_df['COUNT']==0))].count()

# Cleaning the data frame and renaming
BRONX_DF.index.values[1]='BRONX'
BRONX_DF = BRONX_DF.drop('BOROUGH')

# Concatinating the dataframes to generate final output
final = pd.concat([QUEENS_DF,BRONX_DF])


# In[11]:

# Generate dataframe to get values for BROOKLYN borough and number of vehicles involved
BROOKLYN_DF = DataFrame({})
BROOKLYN_DF['ONE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BROOKLYN')&(vehicle_df['COUNT']==1)].count()
BROOKLYN_DF['TWO_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BROOKLYN')&(vehicle_df['COUNT']==2)].count()
BROOKLYN_DF['THREE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BROOKLYN')&(vehicle_df['COUNT']==3)].count()
BROOKLYN_DF['MORE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='BROOKLYN')&((vehicle_df['COUNT']>3)|(vehicle_df['COUNT']==0))].count()

# Cleaning the data frame and renaming
BROOKLYN_DF.index.values[1]='BROOKLYN'
BROOKLYN_DF = BROOKLYN_DF.drop('BOROUGH')

# Concatinating the dataframes to generate final output
final = pd.concat([final,BROOKLYN_DF])


# In[12]:

# Generate dataframe to get values for MANHATTAN borough and number of vehicles involved
MANHATTAN_DF = DataFrame({})
MANHATTAN_DF['ONE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='MANHATTAN')&(vehicle_df['COUNT']==1)].count()
MANHATTAN_DF['TWO_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='MANHATTAN')&(vehicle_df['COUNT']==2)].count()
MANHATTAN_DF['THREE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='MANHATTAN')&(vehicle_df['COUNT']==3)].count()
MANHATTAN_DF['MORE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='MANHATTAN')&((vehicle_df['COUNT']>3)|(vehicle_df['COUNT']==0))].count()

# Cleaning the data frame and renaming
MANHATTAN_DF.index.values[1]='MANHATTAN'
MANHATTAN_DF = MANHATTAN_DF.drop('BOROUGH')

# Concatinating the dataframes to generate final output
final = pd.concat([final,MANHATTAN_DF])


# In[13]:

# Generate dataframe to get values for STATEN ISLAND borough and number of vehicles involved
STATEN_ISLAND_DF = DataFrame({})
STATEN_ISLAND_DF['ONE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='STATEN ISLAND')&(vehicle_df['COUNT']==1)].count()
STATEN_ISLAND_DF['TWO_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='STATEN ISLAND')&(vehicle_df['COUNT']==2)].count()
STATEN_ISLAND_DF['THREE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='STATEN ISLAND')&(vehicle_df['COUNT']==3)].count()
STATEN_ISLAND_DF['MORE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='STATEN ISLAND')&((vehicle_df['COUNT']>3)|(vehicle_df['COUNT']==0))].count()

# Cleaning the data frame and renaming
STATEN_ISLAND_DF.index.values[1]='STATEN ISLAND'
STATEN_ISLAND_DF = STATEN_ISLAND_DF.drop('BOROUGH')

# Concatinating the dataframes to generate final output
final = pd.concat([final,STATEN_ISLAND_DF])


# In[14]:

# Generate dataframe to get values for UNKNOWN borough renamed an NYC and number of vehicles involved
NYC_DF = DataFrame({})
NYC_DF['ONE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='NYC')&(vehicle_df['COUNT']==1)].count()
NYC_DF['TWO_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='NYC')&(vehicle_df['COUNT']==2)].count()
NYC_DF['THREE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='NYC')&(vehicle_df['COUNT']==3)].count()
NYC_DF['MORE_VEHICLE_INVOLVED'] = vehicle_df[(vehicle_df['BOROUGH']=='NYC')&((vehicle_df['COUNT']>3)|(vehicle_df['COUNT']==0))].count()

# Cleaning the data frame and renaming
NYC_DF.index.values[1]='NYC'
NYC_DF = NYC_DF.drop('BOROUGH')

# Concatinating the dataframes to generate final output
final = pd.concat([final,NYC_DF])


# In[23]:

final = final.rename_axis("BOROUGH", axis=1)


# In[24]:

final.head()


# In[25]:

# Generate the file path by joining the directory path and file name for output csv file
op_filename = 'q1_part_2.csv'
op_file_path = os.path.join(current_dir,'output')

# Create output filepath
if not os.path.exists(op_file_path):
    os.mkdir(op_file_path)

# Get the file name
file_name = op_filename
file_path = os.path.join(op_file_path, file_name)


# In[26]:

#Save file to created output file
final.to_csv(file_path)


# In[ ]:



