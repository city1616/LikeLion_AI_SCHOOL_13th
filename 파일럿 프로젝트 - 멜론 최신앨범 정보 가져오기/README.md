## 파일럿 프로젝트
## 주제 : 멜론 최신앨범, TOP100 분석
<hr>

### 과제 개요
* 멜론 홈페이지에서 최신앨범 정보 크롤링 후, CSV 파일로 저장 [코드](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_release_album.py) | [notebook](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_release_album.ipynb) | [CSV](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/2021_09_16_최신앨범정보.csv)
* 멜론 차트의 TOP100 정보 크롤링 후, CSV 파일로 저장 [코드](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_TOP100.py) | [notebook](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_TOP100.ipynb) | [CSV](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/2021_09_16_melon_TOP100.csv)

### 데이터 수집 전략
* 멜론의 최신앨범(국내, 해외) 정보를 크롤링 한다.
	* selenium, xpath를 이용한다.
	* 앨범명, 아티스트, 좋아요 수, 수록곡 수, 발매일의 정보를 가져온다.
	* DataFrame 생성 후, CSV 파일로 저장한다.
	* CSV 파일명 : 크롤링한 날짜_최신앨범정보.csv

* 멜론 차트의 TOP100 곡의 정보를 크롤링 한다.
	* selenium, xpath를 이용한다.
	* 곡명, 아티스트, 좋아요, 앨범명의 정보를 가져온다.
	* DataFrame 생성 후, CSV 파일로 저장한다.
	* CSV 파일명 : 크롤링한 날짜_melon_TOP100.csv

### 데이터 분석 전략
* dataframe의 정보를 살펴본다.
* 좋아요 수를 정수형으로 형 변환한 후 정렬, 상위 데이터의 정보를 살펴본다.
* 좋아요 수가 1000 이상인 데이터를 찾아본다.

<!--
### [파일럿 프로젝트(selenium을 이용한 멜론 음악 정보 크롤링)](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/tree/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기)
* 멜론 홈페이지에서 최신앨범 정보 크롤링 후, CSV 파일로 저장 [PAGE](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_release_album.py) | [notebook](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_release_album.ipynb) | [CSV](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/2021_09_16_최신앨범정보.csv)
* 멜론 차트의 TOP100 정보 크롤링 후, CSV 파일로 저장 [PAGE](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_TOP100.py) | [notebook](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/melon_TOP100.ipynb) | [CSV](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/02.%20웹과%20Github%20기본/05_web_data/파일럿프로젝트_멜론_최신앨범_정보_가져오기/2021_09_16_melon_TOP100.csv)
-->