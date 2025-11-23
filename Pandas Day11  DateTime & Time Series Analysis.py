#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.DataFrame({
    "Date": ["2024-01-01", "2024-02-15", "2024-03-10"],
    "Sales": [1200, 1500, 900]
})
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")


# In[5]:


df.resample("ME").sum()


# In[6]:


df.resample("D").ffill()


# In[7]:


df.resample("W").mean()


# In[8]:


df.resample("W-FRI").sum()


# In[10]:


df.resample("QE").sum()


# In[12]:


df.resample("YE").mean()


# In[13]:


df.resample("BME").sum()


# In[14]:


df.resample("2D").sum()


# In[ ]:




