# 2021_09_08_5
# 코스닥 정보에 대한
# 지수 정보 20210908_14_index.csv
# 시황정보 뉴스 20210908_14_news.csv
# 시황정보 리포트 20210908_14_report.csv
# 인기검색어 20210908_14_pop_word.csv
# 가장 많이 본 뉴스 20210908_14_cnt_news.csv

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml", from_encoding = 'euc-kr')
# print(soup.title)

# 코스닥 정보 가져오기
kosdaq_info = soup.find("em", id = "now_value")
print("코스닥 :", kosdaq_info.text)
index = list(kosdaq_info)

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
# print(high_52)
print("52주최고 :", high_52[2].text)
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
report = []
for one in news[1].find_all("span", class_ = "tit") :
    print(one.text)
    report.append(one.text)
print()

# 인기검색어
pop = soup.find_all("table", class_ = "type_r1")
pop_word = []
# print(len(fav[0].find_all("a")))
print("인기순위")
for idx, one in enumerate(pop[0].find_all("a")) :
    print(idx + 1, ". ", one.text , sep = "")
    pop_word.append(one.text)

# 가장 많이 본 뉴스 정보
pop_news = soup.find_all("ul", class_ = "right_list_1_2")
cnt_news = []
# print(len(pop_news))
for idx, one in enumerate(pop_news[0].find_all("a")) :
    print(idx + 1, one.text)
    cnt_news.append(one.text)

# csv 파일 생성
data_kosdaq = pd.DataFrame({"코스닥" : kosdaq_info}, index = [0])
data_news = pd.DataFrame({"시황뉴스" : news_list})
data_report = pd.DataFrame({"시황정보 리포트" : report})
data_pop_word = pd.DataFrame({"인기검색어" : pop_word})
data_cnt_news = pd.DataFrame({"가장 많이 본 뉴스" : cnt_news})
# print(data_kosdaq)
# print(data_news)
# print(data_report)
# print(data_pop_word)
# print(data_cnt_news)
# data_kosdaq.to_csv("지수_정보_20210908_index.csv", index = False)
# data_news.to_csv("시황정보_뉴스_20210908_news.csv", index = False)
# data_report.to_csv("시황정보_리포트_20210908_report.csv", index = False)
# data_pop_word.to_csv("인기검색어_20210908_pop_word.csv", index = False)
# data_cnt_news.to_csv("가장_많이_본_뉴스_20210908_cnt_news.csv", index = False)
df1 = pd.read_csv("지수_정보_20210908_index.csv")
df2 = pd.read_csv("시황정보_뉴스_20210908_news.csv")
df3 = pd.read_csv("시황정보_리포트_20210908_report.csv")
df4 = pd.read_csv("인기검색어_20210908_pop_word.csv")
df5 = pd.read_csv("가장_많이_본_뉴스_20210908_cnt_news.csv")
# result = pd.merge(df1, df2, how = "left")
result_df = pd.concat([df1, df2, df3, df4, df5], axis = 1)
# print(result_df)
result_df.to_csv("merge_result.csv", index = False)