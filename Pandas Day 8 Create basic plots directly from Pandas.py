#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Day 8 Objectives

By the end of today, you’ll be able to:

Create basic plots directly from Pandas.

Plot line, bar, histogram, and pie charts.

Customize visual styles, colors, and labels.

Use multiple plots (subplots) for better comparison.
    
Practice with real dataset visualizations


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [2500, 2700, 3000, 2800, 3500, 4000],
    'Expenses': [2000, 2200, 2500, 2400, 2700, 3000]
}

df = pd.DataFrame(data)
print(df)


# In[2]:


df.plot(x='Month', y='Sales', kind='line', marker='o', title='Monthly Sales')
plt.ylabel('Sales in USD')
plt.show()


# In[3]:


df.plot(x='Month', y=['Sales', 'Expenses'], kind='line', marker='o')
plt.title('Sales vs Expenses Over Time')
plt.show()


# In[5]:


# Vertical bar
df.plot(x='Month', y='Sales', kind='bar', color='skyblue', title='Sales by Month')
plt.show()


# In[6]:


# Horizontal bar
df.plot(x='Month', y='Sales', kind='barh', color='orange', title='Sales by Month (Horizontal)')
plt.show()


# In[7]:


#Pie Chart
#Pie charts are for showing proportions.
sales_by_region = pd.Series({
    'Nairobi': 45000,
    'Mombasa': 25000,
    'Kisumu': 15000,
    'Eldoret': 20000
})

sales_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Sales Distribution')
plt.ylabel('')
plt.show()


# In[8]:


#Histogram
#Used to visualize the distribution of numeric data.
df['Sales'].plot(kind='hist', bins=5, color='purple', title='Sales Distribution')
plt.xlabel('Sales')
plt.show()


# In[9]:


#Box Plot
#Shows data spread, median, and outliers.
df[['Sales', 'Expenses']].plot(kind='box', title='Sales & Expenses Summary')
plt.show()


# In[11]:


#Scatter Plot
#Useful for showing relationships between two variables.
df.plot(kind='scatter', x='Sales', y='Expenses', color='red', title='Sales vs Expenses')
plt.show()


# In[13]:


#Customizing Your Plots
#Add titles, labels, grids, and legends.
ax = df.plot(x='Month', y='Sales', kind='line', color='green', marker='o')
ax.set_title('Customized Sales Trend')
ax.set_xlabel('Month')
ax.set_ylabel('Sales ($)')
ax.grid(True)
plt.show()


# In[ ]:


Visualization	Function	Example
Line chart	kind='line'	df.plot(x='Month', y='Sales')
Bar chart	kind='bar' / barh	Compare categories
Pie chart	kind='pie'	Show proportions
Histogram	kind='hist'	Show distribution
Box plot	kind='box'	Show spread & outliers
Scatter plot	kind='scatter'	Show variable relationships

