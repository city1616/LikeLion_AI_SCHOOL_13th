# 2021_09_08_6

from urllib.request import urlopen
from bs4 import BeautifulSoup

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