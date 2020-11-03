import requests
from bs4 import BeautifulSoup
import xlwt

# def main(page):
#     url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
#     html = request_douban(url)
#     soup = BeautifulSoup(html,'lxml')
#     save_to_excel(soup)

# def request_douban(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#     except requests.RequestException:
#         return None
url = 'https://movie.douban.com/top250'
#url = 'https://maoshao.ml'
response = requests.get(url)
html = response.text
print(response.status_code)
# if response.status_code == 200:
#     html = response.text
# else:
#     html = None
# soup = BeautifulSoup(html,'lxml')
# print(soup.getText)