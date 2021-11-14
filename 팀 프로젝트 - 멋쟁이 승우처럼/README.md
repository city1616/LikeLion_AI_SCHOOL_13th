## 프로젝트명 : 가스공급량 수요예측 모델개발

### 팀원 : 문승우, 정진우, 오소영, 강수정

### 1. 프로젝트 목표
- 지금까지 배운 내용을 토대로 실전 분석 대회([DACON](https://dacon.io/competitions/official/235830/overview/description))에 참여하여 팀원 전체의 실전 역량을 향상시킨다.
- 데이터 시각화를 통해 데이터의 특징점을 찾아 데이터를 한눈에 확인할 수 있도록 분석한다.
- 데이터가 의미하는 바를 쉽게 확인할 수 있도록 시각화하여 데이터 활용도를 향상시킨다.
- 가스 공급량을 예측하는 머신러닝(또는 딥러닝) 모델을 구축 및 평가한다.
- 다양한 모델의 비교를 통해 최적의 모델을 구축하고 적용한다. 

### 2. 데이터 수집 및 전처리
1. 가스공급량 데이터 
2. 테스트 데이터
3. 서울 기상 데이터
 
### 3. 데이터 분석

### 4. 머신러닝 모델 구축

### 5. 향후 계획 
  
### 기술스택
- 머신러닝 알고리즘(데이터 탐색, 모델 구축 및 평가)
	- 지도학습 : Regression, Decision Tree, Ensemble(RandomForest, lightgbm, xgboost 등)
	- 비지도학습 : K-means, PCA 등
- 시각화 라이브러리 : matplotlib, seaborn

<!--
1. 주제
	- 주제 및 목표    
2. 데이터 수집 및 전처리
	- 데이터 출처
	- 데이터 수집
	- 데이터 전처리(가공) 
3. 데이터 분석
	- 분석 과정
	- 데이터 시각화 및 분석
4. 머신러닝 모델 비교
	- 모델별 공급량 예측
	- 모델별 mse
	- 모델별 캐글 점수 
5. 결론



X = train[["year", "month", "day", "hour", "weekday", "구분_int", "기온(°C)"]]
y = train["공급량"]
GridSearchCV 최적 파라미터 :  {'learning_rate': 0.01, 'max_depth': 12, 'n_estimators': 2000}
GridSearchCV 최고 정확도 : 0.9696

X = train[["month", "hour", "구분_int", "기온(°C)"]]
y = train["공급량"]
GridSearchCV 최적 파라미터 :  {'learning_rate': 0.01, 'max_depth': 12, 'n_estimators': 2000}
GridSearchCV 최고 정확도 : 0.9696
-->