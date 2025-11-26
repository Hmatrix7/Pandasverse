#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.DataFrame({
    "Region": ["East", "West", "East", "South", "West"],
    "Salesperson": ["A", "B", "C", "A", "C"],
    "Sales": [120, 200, 150, 300, 250]
})

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Salesperson",
    aggfunc="sum",
    fill_value=0
)

print(pivot)


# In[2]:


pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Salesperson",
    aggfunc=["sum", "mean", "count"]
)


# In[3]:


arrays = [
    ["Kenya", "Kenya", "Uganda", "Uganda"],
    ["2024", "2025", "2024", "2025"]
]

index = pd.MultiIndex.from_arrays(arrays, names=("Country", "Year"))

df = pd.DataFrame({"GDP": [120, 140, 90, 110]}, index=index)
print(df)


# In[4]:


df.loc["Kenya"]
df.loc[("Kenya", "2024")]


# In[5]:


df = df.unstack()
df.stack()


# In[6]:


pd.melt(df, id_vars=["Region"], var_name="Metric")


# In[ ]:




