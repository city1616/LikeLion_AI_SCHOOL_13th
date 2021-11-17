# Step 1. API key 발급받기
# 회원가입

# Step 2. 미리보기
# API를 사용하여 도시별 날씨 정보를 출력하는 프로그램
# apikey = "193f6fc93b801116d7a263616f6c9c81"

# Step 3. API 알아보기
# API -> Application Programming Interface, 응용 프로그램 프로그래밍 인터페이스
# Client ----- API ----- Server
# API를 만든다		-> 사용자가 필요로 하는 기능을 만들고, 서버에 올려놓은 뒤, 특정한 규약에 따라 사용할 수 있게 하는 프로그램을 만드는 것
# API를 사용한다 	-> 누군가가 만들어놓은 기능을 특정한 규약에 맞춰 사용하는 것
# API 			-> 사용자가 만드는 프로그램과 기존에 있는 프로그램을 연결해 주는 다리
# Openweathermap API 사용
# OpenAPI 		-> 비용을 지불하지 않아도 누구나 사용할 수 있도록 공개된 API

# Step 4. API key 알아보기
# API key -> API를 누가 사용하는지 확인, API key로 누가 누군지 구분

# Step 5. API 링크 만들기
# f-string
city = "Seoul"
apikey = "193f6fc93b801116d7a263616f6c9c81"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}" # API server 주소
print(api) # http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=193f6fc93b801116d7a263616f6c9c81

# Step 6. 날씨 받아오기
# api 주소 ? 앞 -> 공통 url
# api 주소 ? 뒤 -> 파라미터
import requests

city = "Seoul"
apikey = "193f6fc93b801116d7a263616f6c9c81"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}" # API server 주소

result = requests.get(api)
print(result)			# <Response [200]>
print(result.text)

# Step 7. 예쁘게 출력하기 1
import requests
import json

city = "Seoul"
apikey = "193f6fc93b801116d7a263616f6c9c81"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}" # API server 주소

result = requests.get(api)
print(result.text)
print(type(result.text)) 		# <class 'str'> -> 문자열

# json -> javascript object notation, 데이터를 주고 받을 때 사용하는 포맷
# json.loads(str) -> 문자열을 json 타입으로 변경
data = json.loads(result.text)
print(type(data))				# <class 'dict'> -> dictionary

# Step 8. 예쁘게 출력하기 2
import requests
import json

city = "Seoul"
apikey = "193f6fc93b801116d7a263616f6c9c81"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}" # API server 주소

result = requests.get(api)
print(result.text)

data = json.loads(result.text)
print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["main"], "입니다.")
print("현재 온도는 ", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
# 최고 기온 : main - temp_max
# 습도 : main - humidity
# 기압 : main - pressure
# 풍향 : wind - deg
# 풍속 : wind - speed

# Step 9. 예쁘게 출력하기 3
import requests
import json

city = "Seoul"
apikey = "193f6fc93b801116d7a263616f6c9c81"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}" # API server 주소

result = requests.get(api)
# print(result.text)

data = json.loads(result.text)
print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.")
print("현재 온도는 ", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
# 습도 : main - humidity
print("습도는 ", data["main"]["humidity"], "입니다.")
# 기압 : main - pressure
print("기압은 ", data["main"]["pressure"], "입니다.")
# 풍향 : wind - deg
print("풍향은 ", data["wind"]["deg"], "입니다.")
# 풍속 : wind - speed
print("풍속은 ", data["wind"]["speed"], "입니다.")

# Step 10. 언어 및 단위 변경하기
# 언어 변경 -> lang 옵션 추가
# 단위 변경 -> units 옵션 추가
import requests
import json

city = "Seoul"
apikey = "193f6fc93b801116d7a263616f6c9c81"
lang = "kr"
# units - metric -> 화씨에서 섭씨로 변경
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric" # API server 주소

result = requests.get(api)
# print(result.text)

data = json.loads(result.text)
print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.")
print("현재 온도는 ", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
# 습도 : main - humidity
print("습도는 ", data["main"]["humidity"], "입니다.")
# 기압 : main - pressure
print("기압은 ", data["main"]["pressure"], "입니다.")
# 풍향 : wind - deg
print("풍향은 ", data["wind"]["deg"], "입니다.")
# 풍속 : wind - speed
print("풍속은 ", data["wind"]["speed"], "입니다.")























