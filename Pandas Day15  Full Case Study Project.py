#!/usr/bin/env python
# coding: utf-8

# In[ ]:


By the end of today you have mastered:

Importing raw data

Cleaning & handling missing values

Feature engineering

Aggregation & pivoting

Time series resampling

Outlier detection

Exporting clean data


# In[50]:


import pandas as pd

df = pd.read_csv("sales_data.csv")


# In[51]:


df.head()


# In[52]:


df.info()


# In[53]:


df.describe(include="all")


# In[54]:


df.isna().sum()


# In[55]:


#Convert date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.set_index("Date")


# In[56]:


#Convert numeric columns
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")


# In[57]:


#Handle missing values
df["Sales"].fillna(df["Sales"].mean(), inplace=True)
df["Price"].fillna(df["Price"].median(), inplace=True)
df["City"].fillna("Unknown", inplace=True)


# In[58]:


#Remove duplicates
df.drop_duplicates(inplace=True)


# In[59]:


#Feature Engineering
#Extract time features:
df["Year"] = df.index.year
df["Month"] = df.index.month
df["Weekday"] = df.index.day_name()
df["Week"] = df.index.isocalendar().week


# In[60]:


#Rolling and cumulative:
df["MA7"] = df["Sales"].rolling(7).mean()
df["Rolling30"] = df["Sales"].rolling(30).mean()
df["CumulativeAvg"] = df["Sales"].expanding().mean()


# In[61]:


#Daily change:
df["DailyChange"] = df["Sales"].diff()
df["PctChange"] = df["Sales"].pct_change() * 100


# In[62]:


#Aggregation & Pivoting
#Group by Product & Month:
monthly_sales = df.groupby(["Product", "Month"])["Sales"].sum().unstack()


# In[64]:


#Pivot Table Example:
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="City",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)
print(pivot)


# In[65]:


#Outlier Detection (Optional)
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["Sales"] < (Q1 - 1.5*IQR)) | (df["Sales"] > (Q3 + 1.5*IQR))]


# In[66]:


#Resampling for Time Series
#Weekly & Monthly:
weekly_sales = df["Sales"].resample("W").sum()
monthly_sales_total = df["Sales"].resample("ME").sum()


# In[67]:


#Save Cleaned & Aggregated Data
df.to_csv("cleaned_sales_data.csv", index=True)
monthly_sales_total.to_csv("monthly_sales.csv")


# In[ ]:




