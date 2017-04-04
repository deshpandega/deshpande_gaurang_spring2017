
# coding: utf-8

# # Q1_Part_One
# 
# #### NYC Vehicle collision analysis
# #### For each month of 2016, find % of collisions in Manhattan out of total 

# In[34]:

# Import statements
from pandas import Series, DataFrame
import pandas as pd, numpy as np, os
from numpy import nan as NA
from datetime import datetime


# In[35]:

# Take relative path for data
current_dir = os.path.dirname('__file__')
data_dir = os.path.join(current_dir, 'Data')
filename = 'vehicle_collisions.csv'

# Generate the file path by joining the directory path and file name for input csv file
file_path = os.path.join(data_dir, filename)


# In[36]:

# Read csv file using pd.read_csv
vehicle_df = pd.read_csv(file_path,sep=',')


# In[37]:

# Replace all null or NA with 0
vehicle_df.fillna('0', inplace=True)


# In[38]:

# Convert the Date field from string to date
vehicle_df['DATE'] = pd.to_datetime(vehicle_df['DATE'])


# In[39]:

# Generate first dataframe for counting number of accidents in Manhattan and during year 2016
df = pd.DataFrame()
df = vehicle_df[(vehicle_df['BOROUGH']=='MANHATTAN')&(pd.DatetimeIndex(vehicle_df['DATE']).year==2016)]

# Remove unwanted columns
df = df.drop(['UNIQUE KEY','TIME','ZIP CODE','LATITUDE','LONGITUDE','LOCATION','ON STREET NAME','CROSS STREET NAME','OFF STREET NAME','PERSONS INJURED','PERSONS KILLED','PEDESTRIANS INJURED','PEDESTRIANS KILLED','CYCLISTS INJURED','CYCLISTS KILLED','MOTORISTS INJURED','MOTORISTS KILLED','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE','VEHICLE 1 FACTOR','VEHICLE 2 FACTOR','VEHICLE 3 FACTOR','VEHICLE 4 FACTOR','VEHICLE 5 FACTOR'], axis = 1)

# Convert the Date from Datetime to month name
df['MONTH'] = df['DATE'].apply(lambda x: x.strftime('%B'))

# Group by according to each month and Borough and keep column headers
df=df.groupby(['MONTH','BOROUGH'],as_index=False).count()

#Clean & rename the output
df = df.drop('BOROUGH',axis=1)
df.columns.values[1]="MANHATTAN"
df.head()


# In[40]:

# Generate second dataframe for counting number of accidents in entire NYC and during year 2016
df1 = pd.DataFrame()
df1 = vehicle_df[pd.DatetimeIndex(vehicle_df['DATE']).year==2016]

# Remove unwanted columns
df1 = df1.drop(['UNIQUE KEY','BOROUGH','TIME','ZIP CODE','LATITUDE','LONGITUDE','LOCATION','ON STREET NAME','CROSS STREET NAME','OFF STREET NAME','PERSONS INJURED','PERSONS KILLED','PEDESTRIANS INJURED','PEDESTRIANS KILLED','CYCLISTS INJURED','CYCLISTS KILLED','MOTORISTS INJURED','MOTORISTS KILLED','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE','VEHICLE 1 FACTOR','VEHICLE 2 FACTOR','VEHICLE 3 FACTOR','VEHICLE 4 FACTOR','VEHICLE 5 FACTOR'], axis = 1)

# Convert the Date from Datetime to month name
df1['MONTH'] = df1['DATE'].apply(lambda x: x.strftime('%B'))

# Group by according to each month and keep column headers
df1 = df1.groupby(['MONTH'],as_index=False).count()

#Clean & rename the output
df1.columns.values[1]="NYC"
df1.head()


# In[41]:

# Generate final output frame by merging both frames
finalFrame = pd.merge(df, df1, on='MONTH')
finalFrame.head()


# In[42]:

#Calculate percentage
finalFrame['PERCENTAGE'] = finalFrame['MANHATTAN']/finalFrame['NYC']*100


# In[43]:

finalFrame.head()


# In[44]:

# Generate the file path by joining the directory path and file name for output csv file
op_filename = 'q1_part_1.csv'
op_file_path = os.path.join(current_dir,'output')

# Create output filepath
if not os.path.exists(op_file_path):
    os.mkdir(op_file_path)

# Get the file name
file_name = op_filename
file_path = os.path.join(op_file_path, file_name)


# In[45]:

#Save file to created output file
finalFrame.to_csv(file_path,index = False)


# In[ ]:



