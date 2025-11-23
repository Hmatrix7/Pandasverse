#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Concatenation (pd.concat)
#Used when you want to stack DataFrames either vertically or horizontally
#Vertical Concatenation (adding more rows)
import pandas as pd

# Sample Data
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [4, 5, 6],
    'Name': ['David', 'Eve', 'Frank']
})


# In[11]:


# Vertical concatenation (stack rows)
df_all = pd.concat([df1, df2], axis=0)
print(df_all)


# In[12]:


#horizontal concatenation
df_all = pd.concat([df1, df2], axis=1)
print(df_all)


# In[16]:


pd.merge(df1, df2, on="ID", how="inner")


# In[17]:


pd.merge(df1, df2, on="ID", how="left")


# In[18]:


pd.merge(df1, df2, on="ID", how="right")


# In[19]:


pd.merge(df1, df2, on="ID", how="outer")


# In[ ]:




