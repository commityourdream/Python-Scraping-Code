#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.sainsburys.co.uk/shop/gb/groceries/great-offers'
r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text,"html5lib")
parent = soup.find_all("div",{"class":"productESpot"})

data = []
for product in parent:
    PName=product.find("p",{"class":"productName"})
    if PName:
        PName=PName.text
        #print (PName)
    else:
        PName=None
    
    promo=product.find("div",{"class":"promoStrapline"})
    if promo:
        promo=promo.text.strip()
        print(promo)
    else:
        promo=None
        
    price= product.find("div",{"class":"pricing"})
    if price:
        price=price.text.strip()
        print(price)
    else:
        price=None
        
    image= product.find("img")    
    if image:
        image=image['src']
        print(image)
    else:
        image=None
    
    source = {'category':'groceries',
              'product_name':PName,
              'promo':promo,
              'price':price,
              'product_image_url':image
             }
    data.append(source)
                    


Data=pd.DataFrame(data)

Data.to_csv('sainsburys_groceries_product_details.csv')
