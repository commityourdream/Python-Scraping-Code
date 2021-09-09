#!/usr/bin/env python
# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

product_categories_url= pd.read_csv('half-price_product_categories_waitrose.csv')

data = []
for i in range(len(product_categories_url)):
    url=product_categories_url['product_category_url'].iloc[i].format(1)
    print(url)
    offer_type= product_categories_url['offer_type'].iloc[i].format(1)
    try:
        count=0
        r=requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        parent = soup.find_all("article",{"data-test":"product-pod"})
        #print(parent)
        for url2 in parent:
            child = url2.find("a",{"data-actiontype":"redirect"})
            product_url = 'https://www.waitrose.com'+ child['href']
            print(product_url)
            #print(child['href'])
            count= count+1
            print(count)
            product_categories_name=url.split('/')[9]
            product_categories_name= product_categories_name.split('_offers?')
            #print(product_categories_name)
            product_categories_name= product_categories_name[0]
            print(product_categories_name)
            source = {'offer_type':offer_type,
                      'product_category_url':url,
                      'product_category_name':product_categories_name,
                      'product_url':product_url}
            data.append(source)
    except Exception as e:
        print(e)
        
Data=pd.DataFrame(data)
Data.to_csv('{}_waitrose_product_urls.csv'.format(offer_type),encoding='utf-8',index=False)
