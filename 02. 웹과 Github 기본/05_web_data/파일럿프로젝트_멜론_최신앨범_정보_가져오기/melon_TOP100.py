# 멜론 홈페이지의 top100 음악의 정보 크롤링
# top100의 곡명, 아티스트, 좋아요, 앨범명 크롤링
# DataFrame 생성 후, CSV 파일로 저장
# CSV 파일명 : 크롤링한 날짜_melon_TOP100.csv


from selenium import webdriver
import pandas as pd
import time
from datetime import datetime

melon_url = "https://www.melon.com/index.htm"
driver = webdriver.Chrome("../DATA/chromedriver")
driver.get(melon_url)

# 멜론차트_TOP100
melon_chart_button = driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/a')
melon_chart_button.click()
time.sleep(1)

# 멜론차트 TOP100 곡명, 아티스트, 좋아요, 앨범명 가져오기
num = ['50', '100']
top100_list = []
artist_list = []
heart_cnt_list = []
album_list = []

for one in num :
    top100 = driver.find_elements_by_xpath(f'//*[@id="lst{one}"]/td[6]/div/div/div[1]/span/a')
    for title in top100 :
        top100_list.append(title.text)
    artist = driver.find_elements_by_xpath(f'//*[@id="lst{one}"]/td[6]/div/div/div[2]')
    for art in artist :
        artist_list.append(art.text)
    heart_cnt = driver.find_elements_by_xpath(f'//*[@id="lst{one}"]/td[8]/div/button/span[2]')
    for heart in heart_cnt :
        if "," in heart.text :
            heart_cnt_list.append(int(heart.text.replace(",", "")))
        else :
            heart_cnt_list.append(int(heart.text))
    album_info = driver.find_elements_by_xpath(f'//*[@id="lst{one}"]/td[7]/div/div/div/a')
    for album in album_info :
        album_list.append(album.text)

# list 길이 확인
print("top100 title list length :", len(top100_list))
print("top100 artist list length :", len(artist_list))
print("top100 heart count list length :", len(heart_cnt_list))
print("top100 album title list length :", len(album_list))

# DataFrame 생성 후 확인
# CSV 파일 생성
data_dict = {"곡 제목" : top100_list, "아티스트" : artist_list, "좋아요" : heart_cnt_list, "앨범" : album_list}
melon_top100 = pd.DataFrame(data_dict)
print(melon_top100)
melon_top100.to_csv("./" + datetime.today().strftime("%Y_%m_%d") + "_melon_TOP100.csv", index = False)