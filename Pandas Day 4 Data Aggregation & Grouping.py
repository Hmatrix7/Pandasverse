#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Objectives

By the end of Day 4, you’ll be able to:

Group data using groupby()

Apply aggregation functions like sum(), mean(), count()

Use multiple aggregations with .agg()

Sort and analyze grouped data


# In[68]:


import pandas as pd
data={
    'product':['A','A','A','B','B','C','C'],
    'region':['East','East','west','East','West','East','West'],
    'sales':[120,100,150,200,180,90,160]
}
df=pd.DataFrame(data)
print(df)


# In[69]:


grouped=df.groupby('product')['sales'].sum()
print(grouped)


# In[70]:


mult_group=df.groupby(['product','region'])['sales'].sum()
print(mult_group)


# In[71]:


#Aggregation Functions
df.groupby('product')['sales'].mean()


# In[72]:


df.groupby('product')['sales'].max()


# In[73]:


df.groupby('product')['sales'].min()


# In[74]:


df.groupby('product')['sales'].sum().sort_values(ascending=False)


# In[75]:


df.groupby('product')['sales'].agg(['sum','max','mean'])


# In[76]:


grouped_df=df.groupby(['product','region'])['sales'].sum().reset_index()
print(grouped_df)


# In[77]:


sales_data = {
    'Product': ['Phone', 'Phone', 'Laptop', 'Laptop', 'Tablet', 'Tablet'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Revenues': [1000, 1200, 2500, 3000, 800, 900],
    'Quantity': [5, 6, 3, 4, 8, 9]
}


# In[78]:


sales_df = pd.DataFrame(sales_data)
print(sales_df)


# In[79]:


Revenue=sales_df.groupby('Product')['Revenues'].sum()
print(Revenue)


# In[80]:


sales_df.groupby('Region')['Quantity'].sum()


# In[81]:


sales_df.groupby('Region')['Quantity'].mean()


# In[82]:


sales_df.groupby('Product')['Revenues'].agg(['sum','mean'])


# In[84]:


sales_df.groupby('Product')['Revenues'].sum().sort_values(ascending=False)


# In[ ]:




