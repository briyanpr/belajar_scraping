import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.nike.com/id/w?q=men%20jordan%20shoes&vst=men%20jordan%20shoes'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)

"""social_media = driver.find_element(By.CLASS_NAME,"l-social-menu")
driver.execute_script("arguments[0].scrollIntoView(true)", social_media)"""

for i in range(80):
    driver.execute_script("window.scrollBy(0,250)")
    time.sleep(1)

"""driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(2)"""

soup = BeautifulSoup(driver.page_source, 'html.parser')
productlist = soup.find_all('div', class_ = 'product-card__body')
productlinks = []

for item in productlist :
    for link in item.find_all('a', class_ = 'product-card__link-overlay', href=True):
        productlinks.append(link['href'])

print(productlinks)
print(len(productlinks))

