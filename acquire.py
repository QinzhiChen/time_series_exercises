#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd


def get_url(item_url):
    items=[]
    for page_no in range(1,3):
        endpoint = str(page_no)
        response = requests.get(
            item_url+'?page='+endpoint).json()['payload']['items']
        print(f'Getting page {endpoint} of 3', end='')
        items.extend(response)
        items_df=pd.DataFrame(items)
        return items_df

def get_store(store_url):
    stores=[]
    while True:
        response = requests.get(store_url)
        data = response.json()
        stores.extend(data['payload']['stores'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
    stores_df=pd.DataFrame(stores)
    return stores_df
    
def sale_url(url1):
    sales=[]
    for page_no in range(1,184):
        endpoint = str(page_no)
        response = requests.get(
            url1+'/sales'+'?page='+endpoint).json()['payload']['sales']
        print(f'Getting page {endpoint} of 183', end='')
        sales.extend(response)
    sales_df=pd.DataFrame(sales)
    return sales_df

def merge_df(url1,stores_url,item_url):
    sales_df=sale_url(url1)
    stores_df=get_store(store_url)
    items_df=get_url(item_url)
    sales_df=sales_df.rename(columns={'store':'store_id'})
    merged_df = pd.merge(sales_df, store_df, how='left', on='store_id')
    merged_df=merged_df.rename(columns={'item':'item_id'})
    data = pd.merge(merged_df, item_df, how='left', on='item_id')
    return data


def data():
    data=pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    return data
