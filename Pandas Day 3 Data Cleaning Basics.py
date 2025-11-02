#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd

data = pd.read_csv("sales_data1.csv")
print(data)


# In[17]:


import pandas as pd

data = pd.read_csv("sales_data1.csv")

# Check for missing values
print(data.isnull())

# Count total missing per column
print(data.isnull().sum())


# In[19]:


# Drop any row with a missing value
data_cleaned = data.dropna()

# Drop columns with missing values
data_no_cols = data.dropna(axis=1)
print(data.dropna())


# In[13]:


# Fill all NaN values with 0
data_filled = data.fillna(0)

# Fill with column mean or specific value
data["Revenue"] = data["Revenue"].fillna(data["Revenue"].mean())

# Forward fill (use last known value)
data_ffill = data.fillna(method="ffill")

# Backward fill
data_bfill = data.fillna(method="bfill")
data_ffill = data.ffill()
data_bfill = data.bfill()



# In[14]:


# Check for duplicates
print(data.duplicated())

# Count total duplicates
print(data.duplicated().sum())


# In[15]:


# Remove duplicates
data_no_dupes = data.drop_duplicates()
print(data_no_dupes)


# In[8]:


data_unique_products = data.drop_duplicates(subset=["Product"])
print(data_unique_products)


# In[ ]:




