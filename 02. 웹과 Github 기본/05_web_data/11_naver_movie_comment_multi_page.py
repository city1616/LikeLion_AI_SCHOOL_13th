# 2021_09_09_4
# 스파이더맨: 뉴 유니버스 댓글 가져오기
# 1 ~ 5 페이지 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

comments = []
basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page="

for i in range(1, 6) :
    page = urlopen(basic_url + str(i))
    soup = BeautifulSoup(page, "html.parser")

    comment_all = soup.find_all("td", class_ = "title")

    for one in comment_all :
        comment = list(one.children)[6].strip()
        comments.append(comment)

for idx, val in enumerate(comments) :
    print(idx + 1, val)

# 영화 댓글 CSV 파일 생성
comment_dict = {"영화댓글" : comments}
comment_df = pd.DataFrame(comment_dict)
print(comment_df)
comment_df.to_csv("./CSV/네이버 영화 댓글 50개.csv")
comment_df.to_excel("./EXCEL/네이버 영화 댓글 50개.xlsx")