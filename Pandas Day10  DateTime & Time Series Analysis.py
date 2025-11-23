#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd

df = pd.DataFrame({
    "Date": ["2024-01-01", "2024-02-15", "2024-03-10"],
    "Sales": [1200, 1500, 900]
})


# In[76]:


#Converting to DateTime
#Convert a column to datetime
df["Date"] = pd.to_datetime(df["Date"])


# In[77]:


df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


# In[78]:


#Extracting Date Components
#Once converted, you can pull out:
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Weekday"] = df["Date"].dt.day_name()
df["Hour"] = df["Date"].dt.hour
df["Week"] = df["Date"].dt.isocalendar().week


# In[79]:


#Sorting by Date
df = df.sort_values("Date")


# In[80]:


#Filtering by Date
#Single date
df[df["Date"] == "2025-01-15"]


# In[81]:


df[(df["Date"] >= "2025-01-01") & (df["Date"] <= "2025-01-31")]


# In[82]:


#Year-based filtering
df[df["Date"].dt.year == 2024]


# In[83]:


#Set Date as Index (Very Important!)
df = df.set_index("Date")


# In[84]:


#Resampling
#Resampling aggregates data into new time periods.
#Daily → Monthly
df.resample("ME").sum()


# In[85]:


df.columns


# In[86]:


#Rolling (Moving Window) Calculations
#7-day moving average
df["MA7"] = df["Sales"].rolling(7).mean()

#30-day moving sum
df["Rolling30"] = df["Sales"].rolling(30).sum()

#Expanding window (grows over time)
df["CumulativeAvg"] = df["Sales"].expanding().mean()


# In[87]:


#Shifting (Lag Features)
#Sales from previous day
df["Lag1"] = df["Sales"].shift(1)

#Difference between days
df["DailyChange"] = df["Sales"].diff()

#Percent change
df["PctChange"] = df["Sales"].pct_change()


# In[88]:


#Time-Based Grouping
#Group by month
df.groupby(df.index.month)["Sales"].sum()


# In[89]:


#Time Series Visualization (Basic)
df["Sales"].plot(figsize=(10,5))


# In[ ]:





# In[ ]:




