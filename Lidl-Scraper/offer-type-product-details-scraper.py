# # offer-type-product-details-scraper

offer_type_product_details_url=pd.read_csv('lidl-Data - Lidl_offer_type_product_urls.csv')

product_details_data = []
for i in range(len(offer_type_product_details_url)):
    url=offer_type_product_details_url['product_url'].iloc[i].format(1)
    print(url)
    product_name= offer_type_product_details_url['product_name'].iloc[i].format(1)
    #print(product_name)
    r=requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    parent = soup.find_all("div",{"class":"page__section"})
    #print(parent)
    for p in parent:
        p_image = p.find('link',{'itemprop':'image'})
        p_image= p_image['href']
        #print(p_image)
        offer_type = soup.find('div',{'class':'breadcrumbs__text'})
        offer_type= offer_type.text
        print(offer_type)
        regular_price = p.find('span',{'class':'visible@sr'})
        if regular_price:
            regular_price = regular_price.text.strip()
            print(regular_price)
        else:
            regular_price = None
        offer_price = p.find('span',{'class':'pricebox__price'})
        if offer_price:
            offer_price = offer_price.text.strip()
        else:
            offer_price = None
            
        pdesc = p.find_all('li')
        dd = []
        if pdesc:
            for p_desc in pdesc:
                product_description = p_desc.text
                dd.append(product_description)
                print('product_description',product_description)
            
        else:
            pdesc = None
        
        source = {'offer_type':offer_type,
                  'product_name':product_name,
                  'product_url':url,
                  'offer_price':offer_price,
                  'regular_price':regular_price,
                  'image_url':p_image,
                  'product_description':'\n'.join(dd)
                 }
        product_details_data.append(source)

print('Done')

Data=pd.DataFrame(product_details_data)

Data.to_csv('Lidl_offer_type_product_details.csv',encoding='utf-8',index=False)




