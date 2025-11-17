#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Day 6 Objectives

By the end of today, you’ll be able to:

Combine DataFrames using concat().

Merge data like SQL joins using merge().

Join DataFrames on indexes.

Handle different join types (inner, outer, left, right).


# In[1]:


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

# Vertical concatenation (stack rows)
result = pd.concat([df1, df2])
print(result)


# In[4]:


result1=pd.concat([df2,df1])
print(result1)


# In[5]:


df3 = pd.DataFrame({
    'Age': [25, 30, 35],
    'City': ['Nairobi', 'Mombasa', 'Kisumu']
})

pd.concat([df1, df3], axis=1)


# In[6]:


pd.concat([df2,df3],axis=1)


# In[7]:


pd.concat([df2,df3],axis=0)


# In[9]:


employees = pd.DataFrame({
    'EmpID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'DeptID': [101, 102, 103, 101]
})

departments = pd.DataFrame({
    'DeptID': [101, 102, 103],
    'Department': ['HR', 'IT', 'Finance']
})

# Merge on a common column
merged = pd.merge(employees, departments, on='DeptID')
print(merged)


# In[ ]:


Join Type	Description	Example
inner	Only matching rows	pd.merge(df1, df2, how='inner', on='key')
left	All rows from left DataFrame	pd.merge(df1, df2, how='left', on='key')
right	All rows from right DataFrame	pd.merge(df1, df2, how='right', on='key')
outer	All rows from both DataFrames	pd.merge(df1, df2, how='outer', on='key')


# In[17]:


df_a = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df_b = pd.DataFrame({'ID': [3, 4, 5], 'City': ['Nairobi', 'Mombasa', 'Kisumu']})

# Different joins
inner_join = pd.merge(df_a, df_b, how='inner', on='ID')
left_join = pd.merge(df_a, df_b, how='left', on='ID')
outer_join = pd.merge(df_a, df_b, how='outer', on='ID')
right_join = pd.merge(df_a, df_b, how='right', on='ID')


# In[21]:


print(inner_join) #inner	Only matching rows	pd.merge(df1, df2, how='inner', on='key')


# In[22]:


print(left_join)


# In[23]:


print(right_join)


# In[24]:


print(outer_join)


# In[25]:


left = pd.DataFrame({'A': ['A0', 'A1', 'A2']}, index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'B': ['B0', 'B1', 'B2']}, index=['K0', 'K2', 'K3'])

left.join(right, how='outer')


# In[ ]:


Concept	Function	Purpose
Concatenate	pd.concat()	Stack DataFrames vertically/horizontally
Merge	pd.merge()	Combine DataFrames based on common column
Join	.join()	Combine DataFrames using index
Join types	inner, outer, left, right	Control merge behavior


# In[ ]:




