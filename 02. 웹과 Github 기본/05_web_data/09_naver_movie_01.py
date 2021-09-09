# 2021_09_09_1 2 3
# 네이버 영화 정보
# 현재 상영작 제목, 평점, 참여명수, 예매율, 개요 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 웹 페이지 소스 가져오기 및 파싱
url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

print(soup.title)

# 상영작 제목
soup_ul_li = soup.find("ul", class_ = "lst_detail_t1").find_all("li")
print(len(soup_ul_li))
print(soup_ul_li[122].find("dt", class_ = "tit").a.text)

# 평점
print(soup_ul_li[4].find("span", class_ = "num").text)

# 참여 명수
print(soup_ul_li[0].find("em").text)

# 예매율
print(soup_ul_li[0].find("dl", class_ = "info_exp").span.text)

# 개요
txt = soup_ul_li[0].find("span", class_ = "link_txt").text
txt_last = txt.replace("\n", "")
txt_last = txt_last.replace("\t", "")
txt_last = txt_last.replace("\r", "")
print(txt_last)

# 감독
# print(len(soup_ul_li[0].find_all("span", class_ = "link_txt")))
# print(soup_ul_li[0].find_all("span", class_ = "link_txt")[1].text)
director_tmp = soup_ul_li[0].find_all("span", class_ = "link_txt")[1].text
director = director_tmp.replace("\n", "")
director = director.replace("\t", "")
director = director.replace("\r", "")
print(director)

# 출연
# print(soup_ul_li[0].find_all("span", class_ = "link_txt")[2].text)
# print(len(soup_ul_li[0].find_all("span", class_ = "link_txt")[1]))
# print(len(soup_ul_li[0].find_all("span", class_ = "link_txt")[2]))
# print(soup_ul_li[122].find_all("span", class_ = "link_txt")[1].text)
# print(soup_ul_li[122].find_all("span", class_ = "link_txt")[2].text)
# print(soup_ul_li[0].find_all("span", class_ = "link_txt")[2])
print(len(soup_ul_li[78].find("dl", class_ = "info_txt1").find_all("span", class_ = "link_txt")))
print(soup_ul_li[78].find("dl", class_ = "info_txt1").find_all("span", class_ = "link_txt")[2].text)
actor_tmp = soup_ul_li[78].find_all("span", class_ = "link_txt")[2].text
actor = actor_tmp.replace("\n", "")
actor = actor.replace("\t", "")
actor = actor.replace("\r", "")
print(actor)

# 제목, 평점, 참여수, 개요
all_title = []
all_score = []
all_people = []
all_category = []
all_rate = []
all_director = []
all_actor = []
for one in soup_ul_li :
    title = one.find("dt", class_ = "tit").a.text
    score = one.find("span", class_ = "num").text
    people = one.find("em").text
    category = one.find("span", class_ = "link_txt").text
    txt_last = category.replace("\n", "")
    txt_last = txt_last.replace("\t", "")
    txt_last = txt_last.replace("\r", "")
    try :
        rate = one.find("dl", class_ = "info_exp").span.text
    except :
        rate = 0
    director_data = one.find_all("span", class_ = "link_txt")[1].text
    director = director_data.replace("\n", "")
    director = director.replace("\t", "")
    director = director.replace("\r", "")

    actor_data = one.find_all("span", class_ = "link_txt")[2].text
    actor = actor_data.replace("\n", "")
    actor = actor.replace("\t", "")
    actor = actor.replace("\r", "")

    all_title.append(title)
    all_score.append(score)
    all_people.append(people)
    all_category.append(txt_last)
    all_rate.append(rate)
    all_director.append(director)
    all_actor.append(actor)

print(len(all_title), len(all_score), len(all_people), len(all_rate), len(all_category), len(all_director), len(all_actor))

for i in range(123) :
    print(all_title[i], all_score[i], all_people[i], all_rate[i], all_category[i], all_director[i], all_actor[i])

# 저장을 위한 csv, xlsx파일 만들기
import pandas as pd
data_dict = {
    "제목" : all_title, "평점" : all_score, "참여명수" : all_people,
    "예매율" : all_rate,
    "개요" : all_category,
    "감독" : all_director
}
movie_info_df = pd.DataFrame(data_dict)
movie_info_df.to_csv("./CSV/네이버영화.csv", index = False)
movie_info_df.to_excel("./EXCEL/네이버영화.xlsx", index = False)