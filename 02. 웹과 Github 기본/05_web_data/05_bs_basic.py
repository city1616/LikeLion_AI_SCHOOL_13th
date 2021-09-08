# 2021_09_08_2
# BeautifulSoup Basic

from urllib.request import urlopen
from bs4 import BeautifulSoup

page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
</div>
<div>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#
soup = BeautifulSoup(page, 'lxml')
# print(soup.title)
#
## 원하는 div 찾기
# one_info = soup.find_all("div")
# print(len(one_info))
# print(one_info[3])

wanted_info = soup.find_all("div")[3]
print(wanted_info)
last_info_multi = wanted_info.find_all("p", class_ = "p3")
print(last_info_multi)

for one in last_info_multi :
    print(one.text)

# 아래 정보 가져오기
# <p class="p3"> [영역1] 필요없는 정보1 </p>
# <p class="p3"> [영역1] 필요없는 정보3 </p>
print()
a = []
for one in soup.find_all("div")[2].find_all("p", class_ = "p3") :
    print(one.text)
    a.append(one.text)

print(a)

# 실습 - 만든 정보를 csv 파일로 만들어보기
import pandas as pd
column = ["p tab text"]
df = pd.DataFrame(a, columns = column)
# df.to_csv("sample.csv")

# children - 자기 자신보다 한단계 낮은 요소를 묶음
print(wanted_info.children)
print(list(wanted_info.children)[9])