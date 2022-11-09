#!/usr/bin/env python
# coding: utf-8

# # Seach_Term_In_Google

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[18]:


res = requests.get('https://www.mondovo.com/keywords/most-searched-words-on-google/')
soup = BeautifulSoup(res.content, 'html.parser')
item = soup.find_all(class_='scroll-box')
item


# In[23]:


soup = BeautifulSoup(res.content, 'html.parser')
soup


# In[25]:


w_s = pd.DataFrame(
    { 
         " items " : item,
    })

w_s.style.set_properties (**{'background-color': 'Green ',                                                   
                                    'color': 'white',                       
                                    'border-color': 'white',
                             'font-weight': 'bold',
                             'font-size': '11px',
                            })


# In[26]:


w_s.to_csv("data.csv")


# In[ ]:




