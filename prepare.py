#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import acquire




def prepare():
    data=pd.read_csv('sales_df.csv')
    data=data.drop(columns=['Unnamed: 0'])
    data.sale_date = data.sale_date.str.replace(' 00:00:00 GMT', '')
    data.sale_date = pd.to_datetime(data.sale_date, format='%a, %d %b %Y')
    plt.hist(data.sale_amount)
    plt.title('sale_amount')
    plt.show()
    data=data.set_index('sale_date')
    data['month']=data.index.strftime('%B')
    data['day of week'] = data.index.day_name()
    data['sales_total']=data['sale_amount']*data['item_price']
    return data



def data1():
    data = acquire.data()
    data.Date = data.Date.astype('datetime64')
    data = data.set_index('Date')
    data['month'] = data.index.month
    data['year'] = data.index.year
    data = data.fillna(0)
    return data


# In[51]:


data1()


# In[ ]:




