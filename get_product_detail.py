import requests
from bs4 import BeautifulSoup


url = "https://www.nike.com/id/t/air-jordan-1-low-se-shoes-xq1gdm/DC6991-400"

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

title = soup.find('h1', class_='headline-2').text.strip()
price = soup.find('div', class_='product-price').text.strip()
color = soup.find('li', class_='description-preview__color-description').text.strip()
desc = soup.find('div', class_='css-1pbvugb').find('p').text.strip()
review = soup.find('li', class_='review').find('h4').text.strip()
print(title, price, color, desc, review)
