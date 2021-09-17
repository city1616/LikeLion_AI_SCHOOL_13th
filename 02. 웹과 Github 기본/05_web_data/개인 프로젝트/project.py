# 전국 치과 데이터 크롤링
# 치과 데이터를 분석해 신설 치과, 폐업 치과 분석

# 병원약국 xpath : //*[@id="header"]/div[2]/ul/li[1]/h2/a
# 세부 조건별 찾기 xpath :  //*[@id="header"]/div[2]/ul/li[1]/div/div/ul/li[1]/ul/li[2]/a
# 병원 규모별 xpath : //*[@id="typeTab01"]
# 치과 : //*[@id="hospTypeList"]/li[8]/a
# 검색 : //*[@id="hosp-form"]/div/div[1]/a
# 엑셀 다운로드 : //*[@id="hosp-form"]/div/div[3]/a

from  selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

# 다운로드 파일 폴더 지정
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : r'/Users/seungwoomun/Documents/Github/LikeLion_13th_DataCourse/02. 웹과 Github 기본/05_web_data/개인 프로젝트'}
options.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(chrome_options = options)

# 건강보험심사평가원 url
url = "https://www.hira.or.kr/main.do" 				
driver = webdriver.Chrome("../DATA/chromedriver", options = options)
driver.get(url)	# url 접속

# implicitly wait
# 10초로 설정하면 페이지가 로딩되는데 10초까지 기다린다.
# 만약 페이지 로딩이 2초에 완료되었다면 더 기다리지 않고 다음 코드 실행한다.
driver.implicitly_wait(10)
# time.sleep(3)

first_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/h2/a')
first_button.click()

second_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/div/div/ul/li[1]/ul/li[2]/a')
second_button.click()
time.sleep(1)

third_button = driver.find_element_by_xpath('//*[@id="typeTab01"]')
third_button.click()
time.sleep(1)

fourth_button = driver.find_element_by_xpath('//*[@id="hospTypeList"]/li[8]/a')
fourth_button.click()
time.sleep(1)

search_button = driver.find_element_by_xpath('//*[@id="hosp-form"]/div/div[1]/a')
search_button.click()
driver.implicitly_wait(10)

excel_down_button = driver.find_element_by_xpath('//*[@id="hosp-form"]/div/div[3]/a')
excel_down_button.click()
time.sleep(1)

chrome_alert = Alert(driver)
chrome_alert.accept()	 # chrome 경고창 확인 버튼 선택 -> 선택 후 다운로드 시작