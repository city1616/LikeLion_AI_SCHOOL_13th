# 2021_09_07_06
# BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 01 우리가 가져올 URL
# 02 내가 원하는 정보의 위치(span, id)
# url : https://finance.naver.com/sise/
# tag : span, id : KOSPI_now
# 코스닥 : KOSDAQ_now
# 코스피200 : KPI200_now

# html 코드를 요청해서 가져온다.
url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)

# 구체적인 html 확인하고, 구조화
soup = BeautifulSoup(page, 'html.parser', from_encoding = 'euc-kr')
KOSPI = soup.find("span", id = "KOSPI_now")
# print(KOSPI)
print("코스피 현재 지수는 : ", KOSPI.text)

KOSDAQ = soup.find("span", id = "KOSDAQ_now")
print("코스닥 현재 지수는 : ", KOSDAQ.text)

KPI = soup.find("span", id = "KPI200_now")
print("KPI200 현재 지수는 : ", KPI.text)

# 인기 검색 종목과 가격 가져오기
a = soup.find("ul", id = "popularItemList")
print(a.text)

data = soup.find("ul", class_ = "lst_pop")
dat_all = data.find_all("a")
value_all = data.find_all("span")

for one in dat_all :
    print(one.text)

for one in value_all :
    print(one.text)