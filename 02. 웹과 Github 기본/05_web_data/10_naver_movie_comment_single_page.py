# 2021_09_09_3
# 스파이더맨: 뉴 유니버스 댓글 가져오기
# 1 페이지 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page=1"
url2 = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page=2"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

print(soup.title)

# 댓글 하나 가져와 보기
comment_all = soup.find_all("td", class_ = "title")
# print(len(comment_all))
# print(list(comment_all[0].children))
# print(len(list(comment_all[0].children)))
# print(list(comment_all[0].children)[6])

# comment = list(comment_all[0].children)[6].replace("\n", "")
# comment = comment.replace("\t", "")x
comment = list(comment_all[0].children)[6].strip()
print(comment)
print("=" * 30)

# 댓글 1 페이지 댓글 모두 가져오기
comments = []
for one in comment_all :
    comment = list(one.children)[6].strip()
    print(comment)
    comments.append(comment)

print(len(comments))
# 댓글 CSV 파일 생성
comment_dict = {"영화댓글" : comments}
comments_df = pd.DataFrame(comment_dict)
print(comments_df)