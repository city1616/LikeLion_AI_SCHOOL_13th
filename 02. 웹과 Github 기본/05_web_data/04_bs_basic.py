# 2021_09_08_01
# beautifulsoup basic

# urlopen 함수
#   - urllib.request - url 처리와 관련된 모듈 패키지.
#   - 패키지.모듈.함수()의 형식으로 실행
#   - urlopen 함수는 URL을 여는 함수이다.

# BeautifulSoup
#   - 파이썬 라이브러리
#   - HTML과 XML 파일로부터 데이터를 쉽게 가져오기 위한 파이썬 라이브러리이다.
#   - bs4의 모듈 안에 있다.

# HTML Parse
#   - HTML 문법 규칙을 따른 문자열을 다른 문법을 기준으로 단어의 의미나 구조를 분석하는 것을 말한다.
#   - 이를 수행하는 프로그램응ㄹ HTML Parser라 한다.

# HTML 파서의 종류
#   - lxml : c로 구현되어 가장 빠름.
#   - html5lib : 웹 브라우저 방식으로 HTML 해석
#   - html.parser
# 특정 parser의 경우, 특정 태그가 포함되지 않는 오류가 있을 수 있다.

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

# 웹 URL로부터 페이지를 가져오기
page = urlopen(url)
print(page)

page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''

soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 태그명 soup.태그명 => 해당되는 요소의 정보를 가져온다.
# print(soup.title)
# print(soup.body)
# print(soup.div)
# print(soup.img)
print(soup.a)
print(soup.a.text)
print(soup.p.text)
print(soup.div.p.text)

# id, class를 활용해서 정보 가져오기 - 하나의 요소(find)
# id, class를 활용해서 정보 가져오기 - 모든 요소(find_all)
print(soup.find("p", id = "p4").text)
print(soup.find_all("p"))

# find, find_all
# 실습하기 - naver와 모든 a태그 요소 가져오기
print(soup.find("a").text)
print(soup.find_all("a"))

# div 요소 정보를 가지고 온 후, p(id="p4")요소 가져오기
print(soup.div.find("p", id = "p4").text)