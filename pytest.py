#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
dt = pd.read_csv("D:\employees.csv")
df = pd.DataFrame(dt)
# print(df)
#information about data set
# print(df.info())

#it prints the shape row and column
# print(df.shape)

#it prints header
# print(df.head())

#display max row
# pd.set_option('display.max_rows',None)
# print(df)

#to check null values
# print(df.isnull())

#to check no. of total values
# print(df.isnull.sum())

#count the genders types
# print(df['Gender'].value_counts())

#count he max salary and min salary
# print(df['Salary'].max())
# print(df['Salary'].min())

#to find the numnbe of teams in dataset
print(df['Team'].value_counts())


# In[ ]:





# In[ ]:




