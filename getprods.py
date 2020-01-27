from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getprods():
    my_url = 'https://www.pohodafestival.sk/en/shop'
    uclient = ureq(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html,'html.parser')
    products = page_soup.findAll("a",{"class":"product"})

    prods = []
    for i in range(4,12):
        ticks = []
        product_url = 'https://www.pohodafestival.sk' + products[i]['href']
        uwuclient = ureq(product_url)
        product_html = uwuclient.read()
        uwuclient.close()
        product_soup =soup(product_html,'html.parser')
        spans = product_soup.findAll('span',{'class':'product-detail-option-container'})
        title = product_soup.find('h1').get_text()
        img = 'https://www.pohodafestival.sk' + product_soup.find('div',{'class':'product-detail-images'}).a.img['src']
        for span in spans:
            # print(title.get_text() + '==' + span.label.get_text() + ':' + span.input['data-stock'])
            ticks.append({'type':span.label.get_text(),'quantity':span.input['data-stock']})
        prods.append({'title':title,'ticks':ticks,'url':product_url,'img':img})
        
    return prods


# for prod in prods:
#     print('===========')
#     print(prod)
#     print('===========')






# browser = webdriver.Firefox()
# browser.get(product_url)
# import time
# time.sleep(2)
# checkbox = browser.find_elements_by_name('form[option]')
# checkbox[1].click()
# html = browser.page_source
# soup = soup(html,'html.parser')
# print(soup('input',{'class':'product-detail-option'}))
# for box in checkbox:
    
#     box.click()

#     html = browser.page_source

#     soup = soup(html,'html.parser')
#     ticksleft = soup.find('input',{'name':'form[count]'})
#     print(ticksleft)
#     time.sleep(1)
# browser.close()
# checkbox.click()



# uwuclient = ureq(product_url)

# product_html = uwuclient.read()

# uwuclient.close()

# product_soup = soup(product_html,'html.parser')

# quantity = product_soup.find('input',{"id":"quantity"})
# print(quantity['max'])

