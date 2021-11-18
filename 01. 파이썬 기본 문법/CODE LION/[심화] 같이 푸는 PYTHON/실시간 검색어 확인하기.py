# Step 1. 미리보기

# Step 2. 크롤러 알아보기
# Crawler - 기는 것, 파충류 / Crawling
# Web Crawler - 웹 페이지의 데이터를 모아주는 소프트웨어
# Web Crawling - 크롤러를 사용해 웹 페이지의 데이터를 추출해 내는 행위

# Step 3. 블록 조립 키트
# pip install requests
import requests
print(requests)

# 함수(Function) - 자주 사용되는 코드들을 묶어놓고 사용할 수 있게 해주는 기능, 반복적인 작업을 줄일 수 있게 도와주는 파이썬 문법
# 모듈(Module) - 자주 쓰는 클래스, 변수, 함수를 모아 놓은 파일

# Step 4. 블록 조립 키트 사용법
# requests 모듈에서 
# get 함수를 꺼내
# 요청을 보내줘
# 자! 여기 응답값! -> get 함수 : return 응답값

# Step 5. 요청하고 응답받기 1
# requests.get(url) -> requests 모듈 안에 있는 get 함수
# requests.get() -> get 요청을 보내는 기능, 
# 요청 -> put / get / post / delete
# 요청(Client) - 응답(Server)
# Client ---> request(www.daum.net의 정보) ---> Server
# Client <--- response(www.daum.net의 정보 HTML) <--- Server
import requests			# 모듈 사용 명시
print(requests.get)

# Step 6. 요청하고 응답받기 2
# get 함수 -> GET 요청을 보내는 기능
# requests.get(url, params = None, **kwargs)
# Parameters -> url, params(optional), **kwargs(optional)
# Return -> requests.Response
# requests.get(url)
# 마을 조립 키트.집 조립 기계(빨간 블록) -> return : 집
# requests.get(url) -> return : requests.response

# Step 7. 요청하고 응답받기 3
import requests

url = "http://www.daum.net"
print(requests.get(url))				# <Response [200]>  / 200 -> 성공
response = requests.get(url)
print(response.text)					#
print(response.url)
print(response.content)
print(response.encoding)
print(response.headers)
print(response.json)
print(response.links)
print(response.ok)
print(response.status_code)

# Step 8. Beautiful Soup 1
import requests
from bs4 import BeautifulSoup 			# 함수, 모듈 이름에 띄어쓰기 사용 불가능
url = "http://www.daum.net/"
reponse = requests.get(url)
# print(response.text)
print(BeautifulSoup(response.text, 'html.parser'))

# Step 9. Beautiful Soup 2
import requests
from bs4 import BeautifulSoup 			# 함수, 모듈 이름에 띄어쓰기 사용 불가능
url = "http://www.daum.net/"
reponse = requests.get(url)
print(type(response.text))									# <class 'str'>
print(type(BeautifulSoup(response.text, 'html.parser')))	# <class 'bs4.BeautifulSoup'>

# Step 10. Beautiful Soup 3
# BeautifulSoup(데이터, 파싱방법)
# 데이터 -> HTML, XML
# 파싱방법(Parsing)
# Parsing -> 데이터를 의미있게 변경하는 작업, 뭉쳐있는 문자열을 의미있는 값으로 분해하고 이런 것들로 이루어진 데이터
# 		  -> 어떤 문장, 어떤 문자열을 분석해서 의미가 있는 데이터들로 변경하는 것
# Parser  -> parsing을 도와주는 프로그램 / html.parser
# BeautifulSoup(response.text, 'html.parser')
import requests
from bs4 import BeautifulSoup
url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title) 						# <title>Daum</title>

# Step 11. Beautiful Soup 4
import requests
from bs4 import BeautifulSoup
url = "http://www.daum.net/"
response = requests.get(url)
print(response.text[:500])
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title) 						# <title>Daum</title>
print(soup.title.string)				# Daum
print(soup.span) 						# 제일 첫 span 태그 출력
print(soup.findAll('span'))				# 모든 span 태그 출력

# Step 12. Beautiful Soup 5
import requests
from bs4 import BeautifulSoup
url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

file = open("daum.html", "w")
file.write(response.text)
file.close()

# Step 13. Beautiful Soup 6
import requests
from bs4 import BeautifulSoup
url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# html 문서에서 모든 a태그를 가져오는 코드
print(soup.findAll("a"))
# html 문서에서 class가 link_favorsch인 a태그를 가져온은 코드
print(soup.findAll("a", "link_favorsch"))
results = soup.findAll("a", "link_favorsch")

# Step 14. 예쁘게 출력하기
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll("a", "link_favorsch")
# print(results)
print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
for result in results :
	print(rank, "위 : ", result.get_text(), "\n")
	rank += 1

# Step 15. 파일로 출력하기
# open(파일, 모드) / 모드 -> r(read), w(write), a(append)
# open("rankresult.txt", "w")
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll("a", "link_favorsch")
# print(results)

search_rank_file = open("rankresult.txt", "w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
for result in results :
	search_rank_file.write(str(rank) + "위:" + result.get_text() + "\n")
	print(rank, "위 : ", result.get_text(), "\n")
	rank += 1

# Step 16. 응용 해보기
# Naver 실시간 검색어 순위 가져오기
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 로봇 접근 방지를 피하기 위해 requests할 때 headers 정보를 입력
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

# span - item_title
results = soup.findAll("span", "item_title")
# print(results)

search_rank_file = open("rankresult.txt", "w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
for result in results :
	search_rank_file.write(str(rank) + "위:" + result.get_text() + "\n")
	print(rank, "위 : ", result.get_text(), "\n")
	rank += 1
























