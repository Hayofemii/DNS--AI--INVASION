#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas
import pandas as pd
data=[['Ayo', 10], ['Imran', 15], ['chunks', 14]]
df=pd.DataFrame (data, columns = ['Name', 'Age'])
df


# In[4]:


data={'Name':['Ayo', 'Imran', 'Chunks'], 'Age':[10, 15, 14]}
df=pd.DataFrame(data)
df


# In[5]:


dict_data = {"State": ["Abia", "Adamawa", "Lagos", "Osun", "Rivers"], "Capital":["Umuhia", "Yola", "Ikeja", "Osogbo", "Portharcout"], "area": [6320, 36917, 3345, 9251, 110777], "Population":[2845380, 3178950, 9113605, 3416959, 5198605]}
df = pd.DataFrame(dict_data)
df


# In[7]:


csv_df = pd.read_csv('Documents/AI_INVASION/AI_Invasion.csv')
csv_df


# In[8]:


Excel_df = pd.read_excel('Documents/AI_INVASION/AI_Invasion.xlsx')
Excel_df


# In[ ]:




