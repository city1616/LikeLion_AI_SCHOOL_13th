# 전국 치과 데이터 크롤링

## 2021_11_30
# 치과 데이터 크롤링
# 치과 데이터 파일 다운로드
# 다운로드 받을 폴더 지정
# 다운로드 받은 파일명 수정 -> 현재시간_파일명

## 추후 작업 내용
# 크롬 브라우저 열지 않고 실행하도록 옵션 변경
# 두개의 다른 데이터 비교 분석

# 병원약국 xpath : //*[@id="header"]/div[2]/ul/li[1]/h2/a
# 세부 조건별 찾기 xpath :  //*[@id="header"]/div[2]/ul/li[1]/div/div/ul/li[1]/ul/li[2]/a
# 병원 규모별 xpath : //*[@id="typeTab01"]
# 치과 : //*[@id="hospTypeList"]/li[8]/a
# 검색 : //*[@id="hosp-form"]/div/div[1]/a
# 엑셀 다운로드 : //*[@id="hosp-form"]/div/div[3]/a

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import os
from datetime import datetime

# 다운로드 파일 폴더 지정 - option 지정
base_path = r'/Users/seungwoomun/Documents/Github/LikeLion_AI_SCHOOL_13th/개인 프로젝트/'
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : base_path}
options.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(chrome_options = options)

# 건강보험심사평가원 url
url = "https://www.hira.or.kr/main.do"
driver = webdriver.Chrome("./DATA/chromedriver", options = options)
driver.get(url)	# url 접속

# implicitly wait
# 10초로 설정하면 페이지가 로딩되는데 10초까지 기다린다.
# 만약 페이지 로딩이 2초에 완료되었다면 더 기다리지 않고 다음 코드 실행한다.
driver.implicitly_wait(10)
# time.sleep(3)

# 병원 약국 메뉴 선택
first_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/h2/a')
first_button.click()

# 세부 조건별 찾기 선택
second_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/div/div/ul/li[1]/ul/li[2]/a')
second_button.click()
time.sleep(1)

# 병원 규모별 선택
third_button = driver.find_element_by_xpath('//*[@id="typeTab01"]')
third_button.click()
time.sleep(1)

# 치과 선택
fourth_button = driver.find_element_by_xpath('//*[@id="hospTypeList"]/li[8]/a')
fourth_button.click()
time.sleep(1)

# 검색 선택
search_button = driver.find_element_by_xpath('//*[@id="hosp-form"]/div/div[1]/a')
search_button.click()
driver.implicitly_wait(10)

# 엑셀 다운로드 버튼 클릭
excel_down_button = driver.find_element_by_xpath('//*[@id="hosp-form"]/div/div[3]/a')
excel_down_button.click()
time.sleep(1)

# 경고창(알림) 확인 선택 -> 다운로드 진행
chrome_alert = Alert(driver)
chrome_alert.accept()	 # chrome 경고창 확인 버튼 선택 -> 선택 후 다운로드 시작

# 다운로드 소요 시간을 위해 15초 기다림
time.sleep(15)

# 다운받은 파일명 수정
now = datetime.now()
current_time = now.strftime("%Y_%m_%d_%H")

file_oldname = os.path.join(base_path, "병원·약국찾기.xls")
file_newname = os.path.join(base_path, current_time + "_병원·약국찾기.xls")

# 년_월_일_시_병원·약국찾기.xls 로 파일명 수정
os.rename(file_oldname, file_newname)