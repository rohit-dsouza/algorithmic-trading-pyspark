#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import random


# In[38]:


stocks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
portfolio = ['B', 'D', 'F']


# In[39]:


#Initialise sentiment scores for stocks
stk_len = len(stocks)
sent_scores = []
for i in range(stk_len):
    x = round(random.uniform(-1, 1), 1)
    sent_scores.append(x)


# In[40]:


#Initialise sentiment scores for portfolio
port_len = len(portfolio)
sent_port = []
for i in range(port_len):
    x = round(random.uniform(-1, 1), 1)
    sent_port.append(x)


# In[41]:


sent_scores


# In[42]:


sent_port


# In[43]:


#Remove stocks which are already in portfolio
for stock in portfolio:
    if(stocks.index(stock)):
        i = stocks.index(stock)
        stocks.pop(i)
        sent_scores.pop(i)


# In[46]:


#Check if stocks need to be sold
for k in range(port_len):
    if(sent_port[k] < 0):
        portfolio.pop(k)
        sent_port.pop(k)

#Code to check current market value of stock and add to total investment (global variable)


# In[47]:


#Rerun code for initial stock buying to use investment
#after selling all stocks to purchase any new stocks


# In[ ]:


#Add new portfolio back to database

