# # offer_type_scraper_product_urls

offer_url = 'https://www.lidl.co.uk/c/super-weekend/c1325/w2'
req = requests.get(offer_url)
print(req.status_code)

soup = BeautifulSoup(req.text,"html5lib")
of_parent=soup.find_all("article",{"class":"product product--tile"})
#of_parent
offer_type_data = []
for child in of_parent:
    product_title= child.find('h3',{'class':'product__title'}).text.strip()
    print(product_title)
    product_url = child.find('a',{'class':'product__body'})
    product_url = 'https://www.lidl.co.uk'+product_url['href']
    #print(product_url)
    
    offer_type_source ={'product_name':product_title,
                        'product_url':product_url}
    
    offer_type_data.append(offer_type_source)

Data=pd.DataFrame(offer_type_data)
Data.to_csv('offer_type_lidl_product_urls7.csv',encoding='utf-8',index=False)