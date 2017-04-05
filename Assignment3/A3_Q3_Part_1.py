
# coding: utf-8

# # Q2_Part_One
# 
# #### Cricket Matches Analysis
# #### Calculate Average score for each team which host and wins a match 
# #### Check which innings the host played and use the host team's innings score for calculation

# In[1]:

# Import statements
from pandas import Series, DataFrame
import pandas as pd, numpy as np, os
from numpy import nan as NA


# In[2]:

# Take relative path for data
current_dir = os.path.dirname('__file__')
data_dir = os.path.join(current_dir, 'Data')
filename = 'cricket_matches.csv'

# Generate the file path by joining the directory path and file name for input csv file
file_path = os.path.join(data_dir, filename)


# In[3]:

# Read csv file using pd.read_csv
cricket_df = pd.read_csv(file_path,sep=',')
cricket_df

# Remove unwanted columns
cricket_df = cricket_df.drop(['match_details','result','scores','date','venue','round','away','win_by_runs','win_by_wickets','balls_remaining','innings1_wickets','innings1_overs_batted','innings1_overs','innings2_wickets','innings2_overs_batted','innings2_overs','D/L_method','target'], axis = 1)


# In[4]:

# Remove unwanted results
# Match abandoned without a ball bowled # No result (abandoned with a toss) # No result # Match cancelled without a ball bowled # # Match abandoned without a ball bowled # No result (abandoned with a toss) # No result # Match cancelled without a ball bowled # Match scheduled to begin at 13:00 local time (09:00 GMT)

cricket_df = cricket_df[(cricket_df['winner']!="Match abandoned without a ball bowled")&(cricket_df['winner']!="No result (abandoned with a toss)")&(cricket_df['winner']!="No result")&(cricket_df['winner']!=np.NaN)&(cricket_df['winner']!="Match cancelled without a ball bowled")&(cricket_df['winner']!="Match scheduled to begin at 13:00 local time (09:00 GMT)")]


# In[5]:

# Remove all indices where winner is not home team
cricket_df = cricket_df[cricket_df['home']==cricket_df['winner']]


# In[6]:

# Create a data frame with home team and innings1 runs if home team played in inning 1
inn1_df = cricket_df.query('home==innings1')[['home','innings1_runs']]


# In[7]:

# Create a data frame with home team and innings2 runs if home team played in inning 2
inn2_df = cricket_df.query('home==innings2')[['home','innings2_runs']]


# In[8]:

# Rename the column containing runs to score in both data frames
inn1_df.columns.values[1]="score"
inn2_df.columns.values[1]="score"


# In[9]:

# Concatinate both data frames to create single final dataframe
final = pd.concat([inn1_df,inn2_df])

# Groupby home team and average for their scores 
final = final.groupby(['home'], as_index=False).mean()


# In[10]:

# Display result
final.head()


# In[11]:

# Generate the file path by joining the directory path and file name for output csv file
op_filename = 'q3_part_1.csv'
op_file_path = os.path.join(current_dir,'output')

# Create output filepath
if not os.path.exists(op_file_path):
    os.mkdir(op_file_path)

# Get the file name
file_name = op_filename
file_path = os.path.join(op_file_path, file_name)


# In[12]:

#Save file to created output file
final.to_csv(file_path,index = False)


# In[ ]:



