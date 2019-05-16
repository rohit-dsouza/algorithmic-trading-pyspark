#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[23]:


df = pd.read_csv('companieslist.csv')


# In[24]:


df.head()


# In[25]:


investment = 1000


# In[30]:


df = df.sort_values(by = 'Sentiment_Score', ascending = 0)


# In[34]:


df.head()


# In[32]:


df_portfolio = pd.DataFrame(columns = ['Stock', 'Buy_Price', 'Shares', 'Total'])


# In[55]:


df_portfolio.head()


# In[69]:


stk_name = []


# In[70]:


stocks = df['Symbol']


# In[84]:


stk_name = []
n = len(prices)
cp_inv = investment
for stk in stocks:
    x = (df.loc[df['Symbol'] == stk, 'Buy_Price']).values
    price = x[0]
    y = (df.loc[df['Symbol'] == stk, 'Sentiment_Score']).values
    senti = y[0]
    if cp_inv == investment:
        if price * 3 > ((2/3) * cp_inv) or senti < 0:
            continue
        else:
            cp_inv = cp_inv - (price * 3)
            temp = price * 3
            print(temp)
            print(cp_inv)
            stk_name.append(stk)
    else:
        if cp_inv - (price * 3) > 0 and senti > 0:
            cp_inv = cp_inv - (price * 3)
            temp = price * 3
            print(temp)
            print(cp_inv)
            stk_name.append(stk)




