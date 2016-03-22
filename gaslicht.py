# encoding=utf8
#! python3
#grab_beslist
# Searches for the price of a product in beslist.nl from command line using proxy
#need to have python, requests and beautifulsoup4 and robobrowser installed

import sys, time, requests, bs4, re, csv, os
reload(sys)
sys.setdefaultencoding('utf8')


def write_csv(price_elektriciteit,price_gas,leveringskosten_elektriciteit,leveringskosten_gas,leverancier,product):
    with open('nrg.csv','a') as out:
        csv_out=csv.writer(out)
#        csv_out.writerow(['id','product','gasprijs_per_m3','prijs_per_Kw','vastrecht_gas','vastrecht_elektriciteit','leverancier'])
        a=product,price_gas,price_elektriciteit,leveringskosten_gas,leveringskosten_elektriciteit,leverancier
        csv_out.writerow(a)    
    return()

#get the details of each product format it to a float and and call write_csv to write the ouput
def get_tarief(url):
    r = requests.get('https://www.gaslicht.com/'+url, "headers=headers")
    r.raise_for_status()
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    leverancier_product=soup.find('article',{'class':'content'}).h1.get_text()
    leverancier_product=leverancier_product.split('-')
    leverancier=leverancier_product[0]
    product=leverancier_product[1]
    price_gas=soup.find_all('div',{'class':'contentCol noteText'})[13].text
    price_gas=price_gas.replace("ct","").replace(u'\xa0', '').replace(' ', '').replace(',', '.')
    price_gas=float(price_gas)/100
    leveringskosten_elektriciteit=soup.find_all('div',{'class':'contentCol contentText oppositeText'})[2].text
    leveringskosten_elektriciteit=leveringskosten_elektriciteit.replace(u'\xa0', '').replace(' ', '').replace(',', '.').replace('€','')
    leveringskosten_elektriciteit=float(leveringskosten_elektriciteit)
    price_elektriciteit=soup.find_all('div',{'class':'contentCol noteText'})[1].text
    price_elektriciteit=price_elektriciteit.replace("ct","").replace(u'\xa0', '').replace(' ', '').replace(',', '.')
    price_elektriciteit=float(price_elektriciteit)/100
    leveringskosten_gas=soup.find_all('div',{'class':'contentCol contentText oppositeText'})[9].text
    leveringskosten_gas=leveringskosten_gas.replace(u'\xa0', '').replace(' ', '').replace(',', '.').replace('€','')
    leveringskosten_gas=float(leveringskosten_gas)
    print('elektriciteit= ',price_elektriciteit,'gasprijs= ',price_gas, leveringskosten_elektriciteit,leveringskosten_gas,leverancier,product)
    write_csv(price_elektriciteit,price_gas,leveringskosten_elektriciteit,leveringskosten_gas,leverancier,product)
    return()
    
#gets the last part of the url for each supplier and contract and uses this to call get_tarief to get details.
def get_url():
    r = requests.get('https://www.gaslicht.com/energievergelijker', "headers=headers")
    r.raise_for_status()
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    product=soup.find_all('h3',{'class':'comparisonListDesc'})
    i=0
    for div in product:
        links=div.find_all('a')
        for a in links:
            get_tarief(a['href'])
            i=i+1
    return()

#main
os.remove('nrg.csv')
with open('nrg.csv','a') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['product','gasprijs_per_m3','prijs_per_Kw','vastrecht_gas','vastrecht_elektriciteit','naam'])

get_url()


 

