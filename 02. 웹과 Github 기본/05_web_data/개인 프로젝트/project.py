# 병원약국 - 세부 조건별 찾기 xpath :  //*[@id="header"]/div[2]/ul/li[1]/div/div/ul/li[1]/ul/li[2]/a

from  selenium import webdriver

url = "https://www.hira.or.kr/main.do" 				# 건강보험심사평가원 url
driver = webdriver.Chrome("./DATA/chromedriver")
driver.get(url)										# url 접속
