# 2021_09_09_5 6
# 텍스트 시각화
# 네이버 영화
# 샹치와 텐 링즈의 전설 댓글 100개 wordcloud

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from wordcloud import WordCloud
from matplotlib import rc
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random
import time

basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=187348&target=after&page="

comments = []
for i in range(1, 101) :
    url = basic_url + str(i)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # print(soup.title)
    soup_td = soup.find_all("td", class_ = "title")
    # print(len(soup_td))
    for one in soup_td :
        comment = list(one.children)[6].strip()
        comments.append(comment)
    time.sleep(1)
# 가져온 댓글 개수, 내용 확인
# print(len(comments))
# for i in comments :
#     print(i)

# 댓글 dataframe 만든 후 csv 파일 생성
comment_dict = {"영화댓글" : comments}
comment_df = pd.DataFrame(comment_dict)
print(comment_df)
comment_df.to_csv("./CSV/샹치와 텐 링즈의 전설 댓글 1000개.csv")

# csv 파일 불러와서 읽기
f = open("./CSV/샹치와 텐 링즈의 전설 댓글 1000개.csv", encoding = "utf-8")
text = f.read()
# print(text)
f.close()

rc('font', family = 'NanumGothic')

# 특정 모양을 가진 wordcloud
mask = Image.open('./DATA/wordcloud_shape.png')
mask = np.array(mask)

# 글씨색 회색 함수
def grey_color_func(word, font_size, position, orientation, random_state = None, **kwargs) :
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# wordcloud 생성, 특정 모양 mask 지정
wcloud = WordCloud('./DATA/D2Coding.ttf', max_words = 1000, relative_scaling = 0.2, mask = mask).generate(text)
wcloud.recolor(color_func = grey_color_func)

plt.figure(figsize = (12, 12))
plt.imshow(wcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()

