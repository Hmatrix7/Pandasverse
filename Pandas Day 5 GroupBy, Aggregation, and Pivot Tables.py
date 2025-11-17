#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


import pandas as pd

# Sample Data
data = {
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Salary': [50000, 60000, 55000, 52000, 61000, 58000, 62000],
    'Experience': [5, 7, 4, 3, 8, 6, 9]
}

df = pd.DataFrame(data)
print(df)


# In[11]:


df.groupby('Department')['Salary'].mean()


# In[16]:


df.groupby('Department')[['Salary','Experience']].agg(['mean','max','min'])


# In[18]:


df.groupby('Department')['Employee'].count()


# In[19]:


# Multiple aggregations
df.groupby('Department').agg({
    'Salary': ['mean', 'sum'],
    'Experience': ['min', 'max']
})


# In[21]:


df.groupby('Department').agg({
    'Salary':['mean','sum'],
    'Experience':['min','max']
})


# In[23]:


df.groupby('Department')['Salary'].agg(lambda x: x.max() - x.min())#Returns the salary range in each department.


# In[24]:


pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    aggfunc='mean'
)


# In[25]:


pd.pivot_table(
    df,
    values=['Salary', 'Experience'],
    index='Department',
    aggfunc={'Salary': ['mean', 'max'], 'Experience': ['min', 'mean']}
)

