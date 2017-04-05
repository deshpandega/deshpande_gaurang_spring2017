
# coding: utf-8

# # Q2_Part_One
# 
# #### Employee Compensation Analysis
# #### Filter by calendar year, Find average salary per employee, average overtime per employee, average total benefit, average total compensation 
# #### Filter out employees with overtime > 0.05 * salary
# #### For resultant employee's job families, calculate total benefit and total compensation
# #### Calculate total benefit / total compensation * 100 and add it in new column

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
employee_df = employee_df.drop(['Year','Organization Group Code','Organization Group','Department Code','Department','Union Code','Union','Job Family Code','Job Code','Job','Other Salaries','Total Salary','Retirement','Health/Dental','Other Benefits'], axis = 1)


# In[4]:

# Sort by Calendar as Year Type
employee_df = employee_df[employee_df['Year Type'] != 'Fiscal']

# Group By Job Family and Employee ID and take mean of all other salaries columns
employee_df = employee_df.groupby(['Job Family','Employee Identifier'], as_index=False).mean()


# In[5]:

# Get all employees whose overtime > 0.05 * Salaries
employee_df = employee_df[(employee_df['Overtime'])>(0.05*employee_df['Salaries'])]


# In[6]:

# Removing the unwanted columns going forward
employee_df = employee_df.drop(['Employee Identifier','Salaries','Overtime'], axis = 1)


# In[7]:

# Group by Job Family and take mean of total benefit and total compensation
employee_df = employee_df.groupby(['Job Family'], as_index=False).mean()


# In[8]:

# Generate new column for Percent_Total_Benefit
employee_df['Percent_Total_Benefit'] = employee_df['Total Benefits']/employee_df['Total Compensation']*100


# In[9]:

# Display the result
employee_df.head()


# In[10]:

# Generate the file path by joining the directory path and file name for output csv file
op_filename = 'q2_part_2.csv'
op_file_path = os.path.join(current_dir,'output')

# Create output filepath
if not os.path.exists(op_file_path):
    os.mkdir(op_file_path)

# Get the file name
file_name = op_filename
file_path = os.path.join(op_file_path, file_name)


# In[12]:

#Save file to created output file
employee_df.to_csv(file_path,index = False)


# In[ ]:



