import pandas as pd
import datetime
import time
from konlpy.tag import Okt
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
import nltk

import seaborn as sns
import platform
from matplotlib import font_manager, rc
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates, ticker

from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

path = "C:/Windows/Fonts/malgun.ttf"
if platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system()=="Darwin":
    rc('font', family='AppleGothic')
else:
    print("Unknown System")
    
matplotlib.rcParams['axes.unicode_minus'] = False

news_data = pd.read_csv("./CSV/05_news_title.csv")

start = time.time() # 코드 시작 시간

title = ""
for idx, val in enumerate(news_data["제목"]) :
    # print(idx, val)
    # title.append(val)
    title = title + val + " "
    if idx % 10000 == 0 :
        print(idx, val)
    
print("title length :", len(title))
print("소요 시간 :", time.time() - start) # 현재시간 - 시작시간 = 실행 시간

t = Okt()
doc_nouns = t.nouns(title)
print(len(doc_nouns))

ko = nltk.Text(doc_nouns, name = "코로나 키워드 뉴스 제목")

most_fre = ko.vocab().most_common(50)

stopwords = ["코로나", "확", "진자", "세", "중", "차", "회", "위", "등", "더", "제"]

new_ko = []
for one_word in ko :
    if one_word not in stopwords :
        new_ko.append(one_word)

cloud_mask = np.array(Image.open("./PNG/cloud_icon6.png"))

data = new_ko.vocab().most_common(1000)

wc = WordCloud(background_color = "white", 
               max_words = 500,
               mask = cloud_mask,
               font_path = '/Library/Fonts/AppleGothic.ttf',
               contour_width = 2,
               contour_color = "steelblue",
               max_font_size = 300).generate_from_frequencies(dict(data))

plt.figure(figsize = (12, 8))
plt.imshow(wc)
plt.axis("off")
plt.gcf().savefig("./PNG/뉴스_제목_wordcloud.png")
plt.show()