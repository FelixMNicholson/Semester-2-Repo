#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Import pandas.
import pandas as pd

#Import movies & ott Datasets 

movies = pd.read_excel('movies.xlsx')

ott = pd.read_csv('ott.csv')

#Sum Movies 'Age' 

movies['Age'].isnull().sum()

#Replace the missing vales Column 'Age' in Movies with 'Others' 

movies['Age'][movies['Age'].isna()]='Others'

#Replace the missing values in the following columns also with Others: Directors, Genres, Country, and Language.

movies['Directors'][movies['Directors'].isna()] = "Others"

movies['Genres'][movies['Genres'].isna()] = "Others"

movies['Country'][movies['Country'].isna()] = "Others"

movies['Language'][movies['Language'].isna()] = "Others"

movies









                    


# In[ ]:





# In[ ]:




