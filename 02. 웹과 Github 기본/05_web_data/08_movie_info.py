# 2021_09_08_6 7

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# url 정보
# tag, id, class 정보
url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 제목 하나 가져오기
tit_data = soup.find("dt", class_ = "tit").find("a").text
print(tit_data)

# 제목 모두 가져오기
tit_all_data = soup.find_all("dt", class_ = "tit")
# print(len(tit_all_data))
movie_title = []
for idx, one in enumerate(tit_all_data) :
    print(idx + 1, one.find("a").text)
    movie_title.append(one.find("a").text)
print(movie_title)
print()

# 평점 점수 가져오기
score_data = soup.find_all("dd", class_ = "star")
# print("point_data length :", len(point_data))
score = []
for idx, one in enumerate(score_data) :
    print(idx + 1, one.find("span", class_ = "num").text)
    score.append(one.find("span", class_ = "num").text)
print(score)
print()

# 예매율 정보 가져오기
ticket_data = soup.find_all("dl", class_ = "info_exp")
ticketing = []
for idx, one in enumerate(ticket_data) :
    print(idx + 1, one.find("span", class_ = "num").text)
    ticketing.append(one.find("span", class_ = "num").text)
print(ticketing)

# 참여 명수 가져오기
person_data = soup.find_all("span", class_ = "num2")
# print(person_data[1].find("em").text)
cnt_person = []
for idx, one in enumerate(person_data) :
    print(idx + 1, one.find("em").text)
    cnt_person.append(one.find("em").text)
print(cnt_person)

# 타이틀, 평점, 평점 참여명수, 예매율
# 파일 만들기
dict_dat = {"영화제목" : movie_title, "평점" : score, "평점 참여명수" : cnt_person}
movie_df = pd.DataFrame(dict_dat)
print(movie_df)