# 2021_09_09_7
# 텍스트 시각화

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 옥션 데이터 정보 가져오기
# url = "http://browse.auction.co.kr/search?keyword=%EA%B0%80%EB%B0%A9&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EA%B0%80%EB%B0%A9&acode=SRP_SU_0100&arraycategory=&encKeyword=%EA%B0%80%EB%B0%A9"
# page = urlopen(url)
# soup = BeautifulSoup(page, 'lxml')
# print(soup.title)
# print(soup.find_all("span", class_ = "text--title"))

from selenium import webdriver

driver = webdriver.Chrome("./DATA/chromedriver")