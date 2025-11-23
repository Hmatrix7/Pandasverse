#!/usr/bin/env python
# coding: utf-8

# In[15]:


#GroupBy Basics
#groupby() lets you split a dataset into groups, run an operation, and combine results.
import pandas as pd

df = pd.DataFrame({
    "City": ["Nairobi", "Nairobi", "Mombasa", "Nakuru", "Nakuru", "Nakuru"],
    "Sales": [1200, 1500, 800, 600, 900, 750],
    "Agent": ["A", "B", "A", "C", "B", "A"]
})


# In[16]:


#Simple GroupBy
#Total sales per city
df.groupby("City")["Sales"].sum()


# In[17]:


#GroupBy Multiple Columns
#Sales per city per agent
df.groupby(["City", "Agent"])["Sales"].sum()


# In[18]:


#Multiple Aggregations
#Compute sum, mean, and count
df.groupby("City")["Sales"].agg(["sum", "mean", "count"])


# In[20]:


#Different agg per column
df.groupby("City").agg({
    "Sales": ["sum", "mean"],
    "Agent": "count"
})


# In[21]:


#Reset Index
#Convert grouped results back into a normal DataFrame:
df.groupby("City")["Sales"].sum().reset_index()


# In[22]:


#Filtering Groups
#Keep only groups with total sales > 2000
df.groupby("City").filter(lambda x: x["Sales"].sum() > 2000)


# In[23]:


#Transform (Broadcast a computed value)
#Add column of each row’s % of total city sales
df["City_Total"] = df.groupby("City")["Sales"].transform("sum")
df["Pct_of_City"] = df["Sales"] / df["City_Total"]


# In[24]:


#Pivot Tables (Excel-style)
#Total sales per city per agent
pd.pivot_table(
    df,
    values="Sales",
    index="City",
    columns="Agent",
    aggfunc="sum",
    fill_value=0
)


# In[25]:


#MultiIndex Basics
#Some groupby or pivot operations create MultiIndex.
#Example MultiIndex
df2 = df.groupby(["City", "Agent"])["Sales"].sum()


# In[26]:


#Select a specific city
df2.loc["Nakuru"]


# In[27]:


#Select specific city + agent
df2.loc[("Nairobi", "A")]


# In[28]:


#Convert MultiIndex back
df2.reset_index()


# In[29]:


#Sorting Groups
#Sort by aggregated value
df.groupby("City")["Sales"].sum().sort_values(ascending=False)


# In[ ]:




