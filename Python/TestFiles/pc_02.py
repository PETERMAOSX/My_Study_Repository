from bs4 import BeautifulSoup
import requests
html = requests.get('https://www.qiushibaike.com/text/')
soup = BeautifulSoup(html.content,'lxml')
links = soup.find_all('div',class_='content')
for link in links:
    print(link.span.get_text())