#lidl-home-page-product-details-scraper

lidl_product_url= pd.read_csv('Lidl-Homepage-Product_Urls.csv')

data = []
for i in range(len(lidl_product_url)):
    url=lidl_product_url['product_url'].iloc[i].format(1)
    print(url)
    product_categories= lidl_product_url['product_categories'].iloc[i].format(1)
    print(product_categories)
    r=requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    parent = soup.find_all("article",{"id":"productbox"})
    #print(parent)
    for child in parent:
        pname = child.find('h1',{'itemprop':'name'}).text.strip()
        print(pname)
        pprice = child.find('div',{'class':'pricebox__price-wrapper'}).text.strip()
        print(pprice)
        p_image = child.find('a')
        product_image = p_image['href']
        #print(product_image)
        pdesc = child.find_all('li')
        #print(pdesc)
        dd = []
        for p_desc in pdesc:
            product_description = p_desc.text
            dd.append(product_description)
            print('product_description',product_description)
        source = {'product_category':product_categories,
                  'product_name':pname,
                  'product_url':url,
                  'offer_price':pprice,
                  'image_url':product_image,
                  'product_description':'\n'.join(dd)
                 }
        data.append(source)
            #print(data)

print('Done')       

Data=pd.DataFrame(data)

Data.to_csv('lidl_homepage_product_details.csv',encoding='utf-8',index=False)
