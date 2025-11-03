#!/usr/bin/env python
# coding: utf-8
#note the sales_data.csv is excel sheet
# In[69]:


import pandas as pd

data = pd.read_csv("sales_data.csv")

# Access a single column
print(data)


# In[82]:


# Access a single column
print(data["ProductName"])


# In[83]:


# Access multiple columns
data["Revenue"] = data["Price"] * data["UnitsSold"]
print(data[["ProductName", "Revenue"]])


# In[84]:


# Using iloc → integer-based indexing
print(data.iloc[4])        #row number


# In[85]:


print(data.iloc[0:5])      # First 5 rows( print(data.head())  # Preview with revenue)


# In[86]:


# Using loc → label-based indexing
print(data.loc[0])         # Access row with index label 0


# In[87]:


print(data.loc[2:6])       # Rows from label 2 to 6


# In[88]:


# Filter rows where Revenue > 1000
print(data[data["Revenue"] > 9999999])


# In[89]:


# Combine conditions with & (and), | (or)
print(data[(data["Revenue"] > 1000) & (data["Region"] == "Mombasa")])


# In[90]:


# Set 'ProductI' column as index
data.set_index("ProductID", inplace=True)
print(data.head())


# In[91]:


data.reset_index(inplace=True)
print(data.head())


# In[ ]:





# In[ ]:





# In[ ]:




