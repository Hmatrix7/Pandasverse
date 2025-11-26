#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

df = pd.read_csv("sales_data.csv")


# In[10]:


df.head()


# In[11]:


df.info()


# In[12]:


df.describe(include="all")


# In[ ]:




