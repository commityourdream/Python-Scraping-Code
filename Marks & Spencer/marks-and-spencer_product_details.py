product_details_data = []
for i in range(len(product_url)):
    url=product_url['product_url'].iloc[i].format(1)
    print(url)
    product_name= product_url['product_name'].iloc[i].format(1)
    offer_type = product_url['offer_type'].iloc[i].format(1)
    r=requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text,"html5lib")
    product_category = soup.find_all("li",{"class":"breadcrumb__item"})
    product_category=product_category[1].text
    print(product_category)
    product_image = soup.find('div',class_="image-grid__item")

    image = product_image.find("img",{'class':"full-width"})
    if image:
        image = image['src']
        print(image)     
    else:
        image = None
    parent_price = soup.find_all("div",{"data-component":"price"})
    #print(parent_price)
    for pp in parent_price:
        offer_price =pp.find('p',class_="price")
        offer_price = offer_price.text.strip().split('£')
        offer_price = '£' + offer_price[1]
        print(offer_price)
        
        regular_price = pp.find('p',class_="price price--previous")
        #print(regular_price)
        if regular_price:
            regular_price = regular_price.text
            regular_price=regular_price.split()[2]
            print(regular_price)
        else:
            regular_price = None
            
    prod_desc = soup.find("p",{"class":"product-description__main"})
    if prod_desc:
        prod_desc = prod_desc.text
        print(prod_desc)
    else:
        prod_desc = None
    source = {'product_category':product_category,
              'product_name':product_name,
              'product_url':url,
              'offer_price': offer_price,
              'regular_price':regular_price,
              'image_url':image,
              'product_description':prod_desc
             }
    product_details_data.append(source)
print('I am Done')

Data = pd.DataFrame(product_details_data)

Data.to_csv('mark-sandspencer_product_details.csv',encoding='utf-8',index=False)

