# 2021_09_08_01
# beautifulsoup basic

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

page = urlopen(url) # 웹 URL로부터 페이지를 가져오기
print(page)