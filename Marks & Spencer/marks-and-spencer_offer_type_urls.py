#!/usr/bin/env python
# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.marksandspencer.com/c/offers#intid=gnav_offers'

r=requests.get(url)
print(r.status_code)


data = []
soup = BeautifulSoup(r.text,"html5lib")
parent=soup.find_all("li",{"class":"carousel__slide-product"})
for p in parent:
    offer_url = p.find("a",{"class":"product"})['href']
    offer_url = 'https://www.marksandspencer.com'+ offer_url
    print(offer_url)
    source = {'offer_url':offer_url}
    
    data.append(source)
    

Data = pd.DataFrame(data)
Data.to_csv('mark-sandspencer_offer_type_urls.csv',encoding='utf-8',index=False)