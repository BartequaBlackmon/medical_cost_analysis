#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# Performing an analysis on the medical cost on based on individuals from different ages and sex

# In[1]:


# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# # Reading the dataset

# In[2]:


df = pd.read_csv("C:/Users/black/OneDrive/Desktop/insurance.csv")


# In[3]:


df.head()


# In[4]:


df.describe()


# # Data cleaning

# In[5]:


df.dtypes


# In[6]:


# Checking for null values
df.isna().sum()


# In[7]:


# Checking for duplicated value
df.duplicated().any(), df.duplicated().sum()


# In[8]:


df.drop_duplicates(inplace=True)


# In[9]:


# Checking for duplicated value
df.duplicated().any(), df.duplicated().sum()


# In[10]:


# Checking data validition
df.select_dtypes(include= 'object').nunique()


# In[11]:


df['sex'].unique()


# In[12]:


df['smoker'].unique()


# In[13]:


df['region'].unique()


# In[14]:


df.describe().round(2)


# In[15]:


# Checking for outliers

fig = make_subplots(rows=1,
                    cols=len(df.select_dtypes(exclude='object').columns),
                    shared_yaxes=False)

for i in np.arange(0, len(df.select_dtypes(exclude='object').columns), 1):
    fig.add_trace(go.Box(y=df.select_dtypes(exclude='object')[df.select_dtypes(exclude='object').columns[i]],
                         name=df.select_dtypes(exclude='object').columns[i]),
                  row=1,
                  col=i+1)

fig.show()


# In[16]:


# Dropping the outlier points from 'bmi'
df=df[df['bmi'] <= 50]


# In[17]:


# Dropping the outlier points from 'charges'
df = df[df['charges'] <= 55000]


# In[18]:


# Checking for outliers again

fig = make_subplots(rows=1,
                    cols=len(df.select_dtypes(exclude='object').columns),
                    shared_yaxes=False)

for i in np.arange(0, len(df.select_dtypes(exclude='object').columns), 1):
    fig.add_trace(go.Box(y=df.select_dtypes(exclude='object')[df.select_dtypes(exclude='object').columns[i]],
                         name=df.select_dtypes(exclude='object').columns[i]),
                  row=1,
                  col=i+1)

fig.show()


# In[19]:


# check
df.info()


# In[20]:


# reset index
df.reset_index(drop=True, inplace=True)


# In[21]:


df.info()


# # Data Analysis

# In[22]:


px.imshow(df.select_dtypes(exclude= 'object').corr(),
         text_auto= True,
         aspect= True,
         color_continuous_scale= 'Blues',
         title= 'correlation coefficient')


# In[23]:


df['age'].value_counts().head(10)


# # Understanding the the most common age group with insurance

# In[24]:


px.bar(df['age'].value_counts())


# # Understanding the most common gender with insurance

# In[25]:


df['sex'].value_counts()


# In[26]:


px.bar(df['sex'].value_counts(),
      color = df['sex'].value_counts().index,
      title = 'The Most common gender with Insurance')


# # Understanding the count of smoker or non-smoker with insurance

# In[27]:


df['smoker'].value_counts()


# In[28]:


px.bar(df['smoker'].value_counts(),
      color = df['smoker'].value_counts().index,
      title = 'The count of smoker or non-smoker with insurance')


# # The count of insurance by Region

# In[29]:


df['region'].value_counts()


# In[30]:


px.bar(df['region'].value_counts(),
      color = df['region'].value_counts().index,
      title = 'The count of Insurance by each Region')


# # The sum of charges by gender

# In[31]:


df.groupby('sex').agg({'charges': 'sum'})


# In[32]:


px.bar(df.groupby('sex').agg({'charges': 'sum'}),
      color = df.groupby('sex').agg({'charges': 'sum'}).index,
      title ='Sum of charges by gender')


# # The sum of charges for each gender by age

# In[33]:


df.pivot_table(index= 'age', columns= 'sex', values = 'charges', aggfunc = 'sum').sample(5)


# In[34]:


px.bar(df.pivot_table(index = 'age', columns= 'sex', values= 'charges', aggfunc= 'sum'),
      facet_col= 'sex',
      title = 'Sum of charges for each gender by age group')


# # The sum of charges for each age by number of childern.

# In[35]:


df.pivot_table(index= 'age', columns= 'children', values= 'charges', aggfunc= 'sum').head(10).round(2)


# In[36]:


px.scatter(data_frame= df,
          x= 'age',
          y= 'charges',
          size= 'children',
          color= 'sex',
          facet_col= 'sex',
          title= 'relationship between age and charges regarding the number of children status')


# In[ ]:




