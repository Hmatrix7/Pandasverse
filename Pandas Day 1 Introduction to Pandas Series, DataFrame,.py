#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


# Series Example
s = pd.Series([10, 20, 30])
print(s)


# In[4]:


# DataFrame Example
data = {
    "Name": ["Joy", "Sam", "Aisha"],
    "Score": [85, 92, 77]
}

df = pd.DataFrame(data)
print(df)


# In[7]:


df = pd.read_csv("sales_data.csv")
print(df)


# In[8]:


print(df.head())
print(df.info())
print(df.shape)


# In[ ]:




