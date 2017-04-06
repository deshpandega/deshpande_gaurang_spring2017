
# coding: utf-8

# # Q4_Part_One
# 
# #### Movie Awards Analysis
# #### Create different columns for different awards nominations and awards won

# In[1]:

# Import statements
from pandas import Series, DataFrame
import pandas as pd, numpy as np, os
from numpy import nan as NA


# In[2]:

# Take relative path for data
current_dir = os.path.dirname('__file__')
data_dir = os.path.join(current_dir, 'Data')
filename = 'movies_awards.csv'

# Generate the file path by joining the directory path and file name for input csv file
file_path = os.path.join(data_dir, filename)


# In[3]:

# Read csv file using pd.read_csv
awards_df = pd.read_csv(file_path,sep=',')

# Remove unwanted columns
awards_df = awards_df.drop(['totalSeasons','Plot','Rated','Response','Language','Title','Country','Writer','Metascore','imdbRating','Director','Released','Actors','Year','Genre','Runtime','Type','Poster','imdbVotes','imdbID'], axis = 1)


# In[4]:

awards_df = awards_df.dropna()


# In[5]:

# Method to extract Total Awards Won
def extractTotalAwardsWon(row):
    won = 0
    if 'win' in row['Awards']:
        value = row['Awards'].split(' win')
        won = value[0]
        if 'Another' in won:
            temp = won.split('Another ')
            won = temp[1]
            if 'Won' in temp[0]:
                temp = temp[0][4:6]
                won = int(won) + int(temp)
    return won


# In[6]:

# Method to extract Total Awards Nominated
def extractTotalAwardsNominations(row):
    nominations = 0
    if 'nomination' in row['Awards']:
        value = row['Awards'].split(' nomination')
        nominations = value[0]
        if '&' in value[0]:
            temp = value[0].split('& ')
            nominations = temp[1]
            if 'Nominated for ' in value[0]:
                val = value[0].split('Nominated for ')
                temp = val[1][:2]
                nominations = int(nominations) + int(temp)
        elif 'Nominated for ' in value[0]:
            val = value[0].split('Nominated for ')
            temp = val[1][:2]
            nom = value[0].split('Another ')
            nominations = int(temp) + int(nom[1])
        elif 'Another ' in value[0]:
            val = value[0].split('Another ')
            nominations = val[1]
    return nominations


# In[7]:

# Method to extract Golden Globe Awards Nominated
def extractGoldenGlobeAwardsNominations(row):
    nominations = 0
    if 'Nominated for ' in row['Awards']:
        value = row['Awards'].split('Nominated for ')
        if ' Golden Globe' in value[1]:
            nominations = value[1].split(' Golden Globe')[0]
    return nominations


# In[8]:

# Method to extract Emmys Awards Nominated
def extractEmmysAwardsNominations(row):
    nominations = 0
    if 'Nominated for ' in row['Awards']:
        value = row['Awards'].split('Nominated for ')
        if ' Primetime Emmy' in value[1]:
            nominations = value[1].split(' Primetime Emmy')[0]
    return nominations


# In[9]:

# Method to extract Oscar Awards Nominated
def extractOscarAwardsNominations(row):
    nominations = 0
    if 'Nominated for ' in row['Awards']:
        value = row['Awards'].split('Nominated for ')
        if ' Oscar' in value[1]:
            nominations = value[1].split(' Oscar')[0]
    return nominations


# In[10]:

# Method to extract BAFTA Awards Nominated
def extractBAFTAAwardsNominations(row):
    nominations = 0
    if 'Nominated for ' in row['Awards']:
        value = row['Awards'].split('Nominated for ')
        if ' BAFTA Film Award' in value[1]:
            nominations = value[1].split(' BAFTA Film Award')[0]
    return nominations


# In[11]:

# Method to extract Golden Globe Awards Won
def extractGoldenGlobeAwardsWon(row):
    won = 0
    if 'Won ' in row['Awards']:
        value = row['Awards'].split('Won ')
        if ' Golden Globe' in value[1]:
            won = value[1].split(' Golden Globe')[0]
    return won


# In[12]:

# Method to extract Emmys Awards Won
def extractEmmysAwardsWon(row):
    won = 0
    if 'Won ' in row['Awards']:
        value = row['Awards'].split('Won ')
        if ' Primetime Emmy' in value[1]:
            won = value[1].split(' Primetime Emmy')[0]
    return won


# In[13]:

# Method to extract Oscar Awards Won
def extractOscarAwardsWon(row):
    won = 0
    if 'Won ' in row['Awards']:
        value = row['Awards'].split('Won ')
        if ' Oscar' in value[1]:
            won = value[1].split(' Oscar')[0]
    return won


# In[14]:

# Method to extract BAFTA Awards Won
def extractBAFTAAwardsWon(row):
    won = 0
    if 'Won ' in row['Awards']:
        value = row['Awards'].split('Won ')
        if ' BAFTA Film Award' in value[1]:
            won = value[1].split(' BAFTA Film Award')[0]
    return won


# In[15]:

# Extract Total Awards Won
awards_df['Awards_won'] = awards_df.apply(extractTotalAwardsWon, axis = 1)

# Extract Total Awards Nominated
awards_df['Awards_nominated'] = awards_df.apply(extractTotalAwardsNominations, axis = 1)


# In[16]:

# Extract Primetime Emmys Awards Nominated
awards_df['Primetime_Emmys_nominated'] = awards_df.apply(extractEmmysAwardsNominations, axis = 1)

# Extract Primetime Emmys Awards Won
awards_df['Primetime_Emmys_won'] = awards_df.apply(extractEmmysAwardsWon, axis = 1)


# In[17]:

# Extract Oscar Awards Nominated
awards_df['Oscar_nominated'] = awards_df.apply(extractOscarAwardsNominations, axis = 1)

# Extract Oscar Awards Won
awards_df['Oscar_won'] = awards_df.apply(extractOscarAwardsWon, axis = 1)


# In[18]:

# Extract Golden Globe Awards Nominated
awards_df['Golden_Globe_nominated'] = awards_df.apply(extractGoldenGlobeAwardsNominations, axis = 1)

# Extract Golden Globe Awards Won
awards_df['Golden_Globe_won'] = awards_df.apply(extractGoldenGlobeAwardsWon, axis = 1)


# In[19]:

# Extract BAFTA Awards Nominated
awards_df['BAFTA_nominated'] = awards_df.apply(extractBAFTAAwardsNominations, axis = 1)

# Extract BAFTA Awards Won
awards_df['BAFTA_won'] = awards_df.apply(extractBAFTAAwardsWon, axis = 1)


# In[20]:

awards_df.head()


# In[21]:

# Generate the file path by joining the directory path and file name for output csv file
op_filename = 'q4_part_1.csv'
op_file_path = os.path.join(current_dir,'output')

# Create output filepath
if not os.path.exists(op_file_path):
    os.mkdir(op_file_path)

# Get the file name
file_name = op_filename
file_path = os.path.join(op_file_path, file_name)


# In[22]:

#Save file to created output file
awards_df.to_csv(file_path,index = False)


# In[ ]:



