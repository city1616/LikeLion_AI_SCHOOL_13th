## 파일럿 프로젝트
## 주제 : 날씨에 따라 고구마 가격은 어떻게 달라질까?

### 1. 목표 및 개요
* 기상 데이터와 고구마 가격 데이터를 수집, 분석, 시각화 해본다.
* 강의 내용에서 배운 다양한 머신러닝 모델(의사결정트리, 선형회귀, 앙상블 등)을 활용해 기상 환경에 따른 고구마 가격을 예측하는 모델을 구축하고, 미래 고구마 가격을 예측해본다.

### 2. 데이터 수집 전략
* [고구마 가격 데이터](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/tree/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/EXCEL/고구마%20가격)
	* 데이터 출처 : [KAMIS 농산물 유통정보](https://www.kamis.or.kr/customer/main/main.do) 
	* 식량작물 / 고구마 / 밤, 등급 : 상품
	* 평균, 평년, 서울, 부산, 대구, 광주, 대전의 고구마 가격 수집
* [기상 데이터](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/tree/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/CSV/기상%20데이터)
	* 데이터 출처 : [기상자료개방포털](https://data.kma.go.kr/cmmn/main.do)
	* 평균기온, 최저기온, 최고기온, 강수량, 풍속, 습도 등 다양한 기상 데이터 수집

### 3. 데이터 전처리  |  [코드](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/CODE/01_data_preprocessing.ipynb)
* 기상 데이터
	* 컬럼명 변경
	* 결측치 확인 후, 일시(날짜) 기준으로 결측치 제거
	* 결측치 제거 후 남은 결측치는 0 또는 앞뒤 데이터로 대체
	* 일시(날짜) 컬럼의 데이터 티입을 datetime으로 변환
	* 강수량, 바람, 습도 데이터의 지점번호, 지점명 컬럼 삭제
	* 기온, 강수량, 바람, 습도 데이터를 병합하여 [weather.csv](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/CSV/기상%20데이터/weather.csv) 파일 생성
* 고구마 가격 데이터
	* 행과 열 전환
	* 컬럼명 수정
	* 첫 행 제거 후, 인덱스 초기화
	* datetime 타입으로 변환하기 위해, year, month, day 컬럼 생성 및 사용해서 일시 컬럼의 데이터 타입을 datetime으로 변환
	* 고구마 데이터 전체를 전처리 한 후 하나의 데이터 프레임으로 병합하여 [sweet_potato_price.csv](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/CSV/고구마%20가격/sweet_potato_price.csv) 파일 생성
* 최종 데이터
	* 기상 데이터와 고구마 가격 데이터를 일시(날짜) 기준으로 병합하여 [result.csv](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/CSV/result.csv) 파일 생성

### 4. 데이터 분석  |  [코드](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/CODE/02_data_analysis.ipynb)
* 전체 고구마 가격 변동 그래프
<img src = "https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/PNG/전체%20고구마%20가격%20변동.png" width = "80%"/>
* 연도별 고구마 가격 비교
<img src = "https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/PNG/연도별%20고구마%20가격%20비교.png" width = "80%"/>

### 5. 머신러닝 모델 구축  |  [코드](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/CODE/03_machine_learning_model.ipynb)
* [머신러닝 모델 정확도](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/PNG/머신러닝%20모델%20정확도.png)
<!-- <img src = "https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/PNG/머신러닝%20모델%20정확도.png" width = "60%"/> -->
| MODEL | 학습용 정확도 | 테스트용 정확도|
| ----- | ---------- | ---------- |
| Linear Regression | 0.1393813353466936 | 0.1584190703818502 |
| Decision Tree | 1.0 | -0.5502246003715252 |
| Random Forest | 0.8811338468470196 | 0.16022258766236408 |
| Ridge | 0.13938133298459965 | 0.1584204578855346 |
| Lasso | 0.13937825724806652 | 0.15846678711731566 |

* [머신러닝 모델 교차 검증](https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/PNG/머신러닝%20모델%20교차%20검증.png)
<!-- <img src = "https://github.com/city1616/LikeLion_AI_SCHOOL_13th/blob/master/파일럿%20프로젝트%20-%20고구마%20가격%20예측/PNG/머신러닝%20모델%20교차%20검증.png" width = "60%"/> -->
| MODEL | 학습용 교차 검증 점수 | 테스트용 교차 검증 점수|
| ----- | ---------- | ---------- |
| Linear Regression | [0.11368321 0.13591501 0.09097696 0.18429343 0.1261977 ] | [-5.52864991e+20  1.88481673e-01  1.40421593e-01  1.76460306e-01
  1.03291185e-01] |
| Decision Tree | [-0.56728235 -0.85927947 -0.53967529 -0.71583105 -0.40768388] | [-0.90425665 -0.42829368 -0.38773471 -0.68552491 -0.53093237] |
| Random Forest | [0.1471839  0.09309386 0.16866402 0.18840964 0.16205428] | [0.21695047 0.17529004 0.15298503 0.13753823 0.07838464] |

### 6. 향후 계획
* 구축한 머신러닝 모델의 정확도가 다소 떨어지는 모습을 보이고 있어서, 날씨 이외에 추가로 고구마 가격에 영향을 주는 데이터를 수집하고 전처리, 분석, 머신러닝 모델 생성 과정을 반복해서 모델의 정확도가 향상될 수 있도록 추가 분석할 계획이다.