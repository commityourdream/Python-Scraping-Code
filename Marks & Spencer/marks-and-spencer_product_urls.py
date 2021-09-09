data = []
offer_type_url= pd.read_csv('marksandspencer-data - mark-sandspencer_offer_type_urls.csv')
offer_type_url.head()
for i in range(len(offer_type_url)):
    url=offer_type_url['offer_url'].iloc[i].format(1)
    offer_type = offer_type_url['offer_type'].iloc[i].format(1)
    print(offer_type)
    r=requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text,"html5lib")
    parent=soup.find_all("div",{"class":"product"})
    #print(parent)
    for child in parent:
        pname = child.find("h3",{"class":"product__title"})
        print(pname)
        if pname:
            pname = pname.text
        else:
            pname = None
        purl = child.find('a')
        if purl:
            purl ='https://www.marksandspencer.com'+ purl['href']
            print(purl)
        else:
            purl = None
            
        source = {'product_name':pname,
                  'product_url': purl,
                  'offer_type':offer_type
                 }
        data.append(source)
print('done')


Data = pd.DataFrame(data)


Data.to_csv('marksandspencer_product_urls.csv',encoding='utf-8',index=False)
