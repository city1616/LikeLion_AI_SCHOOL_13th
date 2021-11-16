# 2021_09_08_3, 4
# BeautifulSoup example
# 코스피 정보 가져오기
# url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml', from_encoding='euc-kr')
print(soup.title)

# 코스피 정보 가져오기
kospi_info = soup.find("em", id = "now_value")
print("코스피 :", kospi_info.text)

# 거래량 천주 정보 가져오기
print("=" * 30)
deal_info = soup.find("td", id = "quant")
print("거래량(천주) :", deal_info.text)

# 장중최고 정보 가져오기
deal_max = soup.find("td", id = "high_value")
print("장중최고 :", deal_max.text)

# 52주최고 정보 가져오기
high_52 = soup.find_all("td", class_ = "td")
# print(len(high_52))
print("52주최고 :", high_52[2].text)
print("=" * 30)

# 투자자별 매매동향
invest = soup.find_all("dd", class_ = "dd")
# print(len(invest_indi))
# print(invest_indi[0].text)
# print(invest_indi[0].find("span").text)
print("--- 투자자별 매매동향 ---")
for one in range(0, 3) :
    print(invest[one].text)
print()

# 프로그램 매매동향
print("--- 프로그램 매매동향 ---")
for one in range(3, 6) :
    print(invest[one].text)
print("=" * 30)

# 시황뉴스
news = soup.find_all("div", class_ = "box_type_m")
# print(len(news))
# print(news[0])
news_list = []
print("--- 시황뉴스 ---")
for one in news[0].find_all("span", class_ = "tit") :
    print(one.text)
    news_list.append(one.text)
print()

# 시황정보 리포트
print("--- 시황정보 리포트 ---")
for one in news[1].find_all("span", class_ = "tit") :
    print(one.text)
print()

# 인기검색어
fav = soup.find_all("table", class_ = "type_r1")
fav_list = []
# print(len(fav[0].find_all("a")))
print("인기순위")
for idx, one in enumerate(fav[0].find_all("a")) :
    print(idx + 1, ". ", one.text , sep = "")
    fav_list.append(one.text)

# 시황뉴스 목록을 csv, xlsx 파일로 만들기
import pandas as pd
data = pd.DataFrame({"시황뉴스" : news_list})
print(data)
# data.to_csv("news.csv", index = False)
# data.to_csv("news_excel.xlsx", index = False)
fav_data = pd.DataFrame({"인기검색어" : fav_list})
print(fav_data)
fav_data.to_csv("인기검색어 순위.csv", index = False)