from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import time

url = 'https://www.nike.com/id/w/mens-football-shoes-1gdj0znik1zy7ok'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)

for i in range(40):  #scroll web
    driver.execute_script("window.scrollBy(0,250)")
    time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
product_list = soup.find_all('div', class_ = 'product-card__body')
productlinks = []

for item in product_list : #get_link
    for link in item.find_all('a', class_ = 'product-card__link-overlay', href=True):
        productlinks.append(link['href'])

print("Jumlah data = ", len(productlinks))


product = []
i = 0
for link in productlinks:

    i = i+1
    print("data ke = ", i) 

    driver.get(link)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    rvw = []
    img = []
    size = []

    title = soup.find('h1', class_='css-16cqcdq').text.strip()
    price = soup.find('div', class_='product-price').text.strip()
    color = soup.find('li', class_='description-preview__color-description').text.strip()
    desc = soup.find('div', class_='css-1pbvugb').find('p').text.strip()

   
    for item in soup.findAll('li', class_='review'):
        review = item.find('h4', class_='review-title').text.strip()
        rvw.append((review))
    

    for item2 in soup.find_all('div', class_="css-1mhv7vq"):
        for image in item2.find_all('img'):
            img.append(image['src'])

    for item3 in soup.find_all('label', class_='css-xf3ahq'):
        sz = item3.text.strip()
        size.append((sz))

    data = {
            'title' : title,
            'link' : link,
            'price' : price,
            'color' : color,
            'size' : size,
            'desc' : desc,
            'review' : rvw,
            'image' : img
        }
    product.append(data)

driver.close()
df = pd.DataFrame(product)
df.to_excel("Men's Football Shoes.xlsx", index=False)
print(df)



