
# coding: utf-8

# # Q2_Part_One
# 
# #### Employee Compensation Analysis
# #### Find highest paid department in each organization group by  calculating mean of total compensation for each department
# #### Organization > Department > highest to lowest compensation

# In[1]:

# Import statements
from pandas import Series, DataFrame
import pandas as pd, numpy as np, os
from numpy import nan as NA


# In[2]:

# Take relative path for data
current_dir = os.path.dirname('__file__')
data_dir = os.path.join(current_dir, 'Data')
filename = 'employee_compensation.csv'

# Generate the file path by joining the directory path and file name for input csv file
file_path = os.path.join(data_dir, filename)


# In[3]:

# Read csv file using pd.read_csv
employee_df = pd.read_csv(file_path,sep=',')

# Remove unwanted columns
employee_df = employee_df.drop(['Year Type','Year','Organization Group Code','Department Code','Union Code','Union','Job Family Code','Job Family','Job Code','Job','Employee Identifier','Salaries','Overtime','Other Salaries','Total Salary','Retirement','Health/Dental','Other Benefits','Total Benefits'], axis = 1)


# In[4]:

# Group by columns and calculate the mean of total compensation
final = employee_df.groupby(['Organization Group','Department'],as_index=False).mean()


# In[5]:

# Sort by Org and then Total Compensation and then department
final = final.sort_values(by=['Organization Group','Total Compensation','Department'],ascending=False)


# In[6]:

final.head()


# In[7]:

# Generate the file path by joining the directory path and file name for output csv file
op_filename = 'q2_part_1.csv'
op_file_path = os.path.join(current_dir,'output')

# Create output filepath
if not os.path.exists(op_file_path):
    os.mkdir(op_file_path)

# Get the file name
file_name = op_filename
file_path = os.path.join(op_file_path, file_name)


# In[8]:

#Save file to created output file
final.to_csv(file_path,index = False)


# In[ ]:



