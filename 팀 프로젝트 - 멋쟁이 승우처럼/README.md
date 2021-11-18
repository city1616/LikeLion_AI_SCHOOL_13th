## 프로젝트명 : 가스공급량 수요예측 모델개발(2021.10.15 ~ 2021.11.10)

### 팀 구성 및역할

 * 문승우 `팀장` - 데이터 전처리, 시각화, 추가 변수 생성, 모델 성능 개선
    * merging dataset and processing missing value</br>
    * feature engineering (using statistics, model)</br>
    * evaluate model (using Cross Validation, Grid Search)</br>
    * evaluation metrics – by MSE, RMSE, finally evaluated by NMAE</br>
    * Cross Validation and Parameter Tuning</br>
    

 * 정진우 `부팀장` - 모델 성능 향상, 발표
    * compare Machine Learning Model
    * Cross Validation and Parameter Tuning


 * 오소영 `팀원` - 데이터 시각화, 발표 자료 준비,PPT 자료 정리
    * Matplotlib, seaborn 등을 활용한 데이터 탐색 및 시각화

* 강수정 `팀원` - 데이터 탐색 및 수집

### 1. 프로젝트 목표
- 지금까지 배운 내용을 토대로 실전 분석 대회([DACON][dacon])에 참여하여 팀원 전체의 실전 역량을 향상시킨다.
- 데이터 시각화를 통해 데이터의 특징점을 찾아 데이터를 한눈에 확인할 수 있도록 분석한다.
- 데이터가 의미하는 바를 쉽게 확인할 수 있도록 시각화하여 데이터 활용도를 향상시킨다.
- 가스 공급량을 예측하는 머신러닝(또는 딥러닝) 모델을 구축 및 평가한다.
- 다양한 모델의 비교를 통해 최적의 모델을 구축하고 적용한다. 

### 2. 데이터 수집 
* 내부 데이터(가스공사) - 2013 ~ 2018년 시간별 공급량 데이터
* 외부 데이터(기상청 기상자료개방포털) - 2013 ~ 2018년 서울 기상 데이터

### 3. 데이터 전처리
 
### 4. 데이터 분석 및 시각화
* 분석 과정
	* .shpae
	* .info()
	* .isnull().sum()
	* describe()

* 데이터 시각화
	* 연도별 월평균 공급량(데이터셋 : 훈련용 공급량 데이터)
	* 연도별 월평균 기온(데이터셋 : 훈련용 기온 데이터)
	* 구분별 월평균 공급량(데이터셋 : 훈련용 공급량 데이터)
	* 데이터간 상관관계(데이터셋 : 훈련용 공급량 + 기온 데이터)
	* 공급량과 기온의 상관관계 그래프(데이터셋 : 훈련용 공급량 + 기온 데이터)
	* 구분별 공급량 분포
	* 예측 대상 일자(년월일시) 확인
	* 예측한 기온 확인(2019년 월평균 기온)

### 5. 머신러닝 모델 구축
* 공급량 예측 모델(기온 데이터 제외)
	* LinearRegression
	* DecisionTreeRegressor
	* RandomForestRegressor
	* GradientBoostingRegressor
	* XGBRegressor
	* LGBMRegressor

### 6. 향후 계획  
  
### 기술스택
- 머신러닝 알고리즘(데이터 탐색, 모델 구축 및 평가)
	- 지도학습 : Regression, Decision Tree, Ensemble(RandomForest, lightgbm, xgboost 등)
	- 비지도학습 : K-means, PCA 등
- 시각화 라이브러리 : matplotlib, seaborn

[//]: # (hello)

   [dacon]: https://dacon.io/competitions/official/235830/overview/description

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


리드미 작성이 잘 되어있어서 멋사 과정 동안 어떤 것을 했는지 간략하게 확인 할 수 있었습니다.
진행한 내용마다 기간이 표시되어 있어 좋았습니다.

깃허브 페이지를 추가로 만들면 좋을 것 같아요!




-->