#!/usr/bin/env python
# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

product_url= pd.read_csv('half-price_waitrose_product_urls.csv')

data = []
for i in range(len(product_url)):
    url=product_url['product_url'].iloc[i].format(1)
    print(url)
    try:
        count=0
        r=requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        parent = soup.find_all("article",{"data-test":"product-content"})
        #print(parent)
        for p in parent:
            product_name = p.find("li",{"class":"currentPage___K9xCe"})
            print(product_name.text)
            if product_name:
                product_name=product_name.text
            else:
                product_name=None
            product_category=p.find_all("a",{"class":"link___TxO4j"})

            if product_category:
                product_category=product_category[1].text
            else:
                product_category= None
            
            offer_price = p.find("span",{"data-test":"product-pod-price"})
            if offer_price:
                offer_price=offer_price.text
            else:
                offer_price = None
            
            regular_price = p.find("span",{"class":"offerDescription___13aL3 underline___1Nvj9"})
            regular_price = regular_price.text.split('Was')
            offer_type = regular_price[0]
            print(offer_type)
            if regular_price:
                regular_price = regular_price[1]
            else:
                regular_price = None
                
            prod_desc = p.find("section",{"id":"marketingDescriptionBop"})
            if prod_desc:
                prduct_description= prod_desc.text
            else:
                prduct_description = None
            
            rating = p.find("span",{"itemprop":"ratingValue"})
            if rating:
                rating= rating.text
            else:
                rating = None
                
            review = p.find("span",{"class":"ratingText___2sGgC"})
            
            if review:
                review = review.text
                print(review)
            else:
                review = None
            
            disclaimer = p.find("section",{"class":"disclaimer___3mXxc"})
            #print(section.text)
            disclaimerText = disclaimer.find('p')
            if disclaimerText:
                disclaimerText=disclaimerText.text
            else:
                disclaimerText = None
            
            img_url = p.find("div",{"class":"detailsContainer___1QKJt"})
            image_url = img_url.find("img")['src']
            if image_url:
                image_url= image_url
            else:
                image_url = None
                
            source = {'offer_type':offer_type,
                      'product_category':product_category,
                      'product_name':product_name,
                      'product_url':url,
                      'offer_price':offer_price,
                      'regular_price':regular_price,
                      'image_url':image_url,
                      'product_description':prduct_description,
                      'review_count':review,
                      'star_rating':rating,
                      'disclaimer':disclaimerText
                     }
            data.append(source)
      
    except Exception as e:
        print(e)
print('Done')

Data=pd.DataFrame(data)
Data.to_csv('half_price_waitrose_product_details.csv'.format(offer_type),index=False)
