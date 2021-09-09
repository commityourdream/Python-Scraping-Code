#!/usr/bin/env python
# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

offer_type=input('enter a offer_type :')
#save-third
#half-price



url = str('https://www.waitrose.com/ecom/shop/browse/offers/highlights/{}').format(offer_type)
print(url)
r = requests.get(url)
print(r.status_code)


#list of product-categories
soup = BeautifulSoup(r.text,"html5lib")
parent = soup.find_all("a",{"class":"link___ZQeXn themeGrey___I1gDh"})
#print(parent['href'])
data = []
for product in parent:
    product_categories_url = 'https://www.waitrose.com'+product['href']
    product_categories_name=product_categories_url.split('/')[9]
    product_categories_name= product_categories_name.split('_offers?')
    #print(product_categories_name)
    product_categories_name= product_categories_name[0]
   
    print(product_categories_name)

    source={'offer_type':offer_type,
            'product_category_name':product_categories_name,
            'product_category_url':product_categories_url}
    #print(source)
    data.append(source)


Data=pd.DataFrame(data)
Data.to_csv('{}_product_categories_waitrose.csv'.format(offer_type),encoding='utf-8',index=False)
