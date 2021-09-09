#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.lidl.co.uk/c/home-refresh/c2020/w2'
r = requests.get(url)
print(r.status_code)

# coming_up /this_week

soup = BeautifulSoup(r.text,"html5lib")
parent=soup.find_all("article",{"class":"product product--tile"})
#print(parent)
count =0
data = []
for product in parent:
    PName=product.find("h3",{"class":"product__title"})
    if PName:
        PName=PName.text
        PName= PName.strip()
        print(PName)
    else:
        PName=None
        
    Purl = product.find("a",{"class":"product__body"})
    if Purl:
        Purl = 'https://www.lidl.co.uk'+Purl['href']
    else:
        Purl = None
        
    heading = soup.find("strong",{"class":"sectionhead__srtitle visible@sr"})
    heading = heading.text
    print(heading)
    
    source = {'product_categories':heading,
              'product_name':PName,
              'product_url':Purl}
    
    data.append(source)
        
    count = count+1
    print(count)


Data=pd.DataFrame(data)
Data.to_csv('lidl_product_urls9.csv',encoding='utf-8',index=False)