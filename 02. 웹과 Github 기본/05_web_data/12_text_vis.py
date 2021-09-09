# 2021_09_09_5
# 텍스트 시각화

import wordcloud
from wordcloud import WordCloud
from matplotlib import rc

print(wordcloud.__version__)
# 파일 읽기 함수 - open()
f = open("./CSV/네이버 영화 댓글 50개.csv", encoding = "utf-8")
text = f.read()
print(text)
f.close()

rc('font', family = 'NanumGothic')

wcloud = WordCloud('./DATA/D2Coding.ttf', max_words = 1000, relative_scaling = 0.2).generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize = (12, 12))
plt.imshow(wcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()