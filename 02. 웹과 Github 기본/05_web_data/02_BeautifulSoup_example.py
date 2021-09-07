# 2021_09_07_06
# BeautifulSoup example

from urllib.request import urlopen
from bs4 import BeautifulSoup

# url
# tag, id, class
# 다우산업지수, 나스닥 종합, S&P 500
# 다우산업지수 : dd, class : point_status

url = "https://finance.naver.com/world/"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser', from_encoding='euc-kr')
print(soup.title)

data = soup.find("ul", id = "worldIndexColumn1")
print(data.span.text)
print(data.strong.text)
print(data.dd.strong.text)

data1 = soup.find_all("dt", class_ = "blind")
print(data1.text)