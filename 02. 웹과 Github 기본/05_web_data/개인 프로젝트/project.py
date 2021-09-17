# 전국 치과 데이터 크롤링
# 치과 데이터를 분석해 신설 치과, 폐업 치과 분석

# 병원약국 - 세부 조건별 찾기 xpath :  //*[@id="header"]/div[2]/ul/li[1]/div/div/ul/li[1]/ul/li[2]/a

from  selenium import webdriver
import time

url = "https://www.hira.or.kr/main.do" 				# 건강보험심사평가원 url
driver = webdriver.Chrome("../DATA/chromedriver")
driver.get(url)										# url 접속

# implicitly wait
# 10초로 설정하면 페이지가 로딩되는데 10초까지 기다린다.
# 만약 페이지 로딩이 2초에 완료되었다면 더 기다리지 않고 다음 코드 실행한다.
driver.implicitly_wait(10)
# time.sleep(3)




first_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/div/div/ul/li[1]/ul/li[2]/a')
first_button.click()