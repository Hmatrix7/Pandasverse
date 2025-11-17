#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Day 7 Objectives

By the end of today, you’ll be able to:

Detect and handle missing values (NaN).

Replace or fill missing values.

Detect and remove duplicates.

Understand how to clean messy data using replace(), map(), and apply().

Prepare clean datasets ready for analysis.


# In[9]:


import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'Age': [25, 30, np.nan, 22, 28],
    'Salary': [50000, np.nan, 55000, 48000, 52000],
    'Experience':[4,5,6,7,8]
}

df = pd.DataFrame(data)
print(df)


# In[10]:


df.isnull()


# In[11]:


df.isnull().sum()


# In[12]:


# Drop rows with missing values
df.dropna()


# In[13]:


# Drop columns with missing values
df.dropna(axis=1)


# In[14]:


# Fill with a fixed value
df.fillna(0)


# In[17]:


# Fill with column mean or median
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)


# In[18]:


df.fillna(method='ffill')  # Forward fill (previous value)
df.fillna(method='bfill')  # Backward fill (next value)


# In[20]:


# Detect duplicates
df.duplicated()


# In[21]:


# Remove duplicates
df.drop_duplicates(inplace=True)


# In[22]:


df['Name'].replace('Bob', 'Robert', inplace=True)


# In[23]:


# Convert all names to uppercase
df['Name'] = df['Name'].apply(lambda x: x.upper() if isinstance(x, str) else x)

# Create a new column based on logic
df['AgeGroup'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')


# In[ ]:


Concept	Function	Description
Detect missing data	isnull() / notnull()	Shows which cells are NaN
Drop missing	dropna()	Removes rows/columns with NaN
Fill missing	fillna()	Replaces NaN with value or method
Duplicates	duplicated() / drop_duplicates()	Detect and remove duplicates
Replace values	replace()	Swap out incorrect or unwanted data
Apply function	apply() / map()	Clean or transform column values


# In[ ]:




