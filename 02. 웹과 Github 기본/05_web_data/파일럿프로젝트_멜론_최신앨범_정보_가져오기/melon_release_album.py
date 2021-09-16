# 멜론 홈페이지의 최신 앨범 정보 크롤링
# 최신앨범(국내, 해외)의 앨범명, 아티스트, 좋아요수, 수록곡수, 발매일 크롤링
# DataFrame 생성 후, CSV 파일로 저장
# CSV 파일명 : 크롤링한 날짜_최신앨범정보.csv

from selenium import webdriver
import pandas as pd
import time
from datetime import datetime

melon_url = "https://www.melon.com/index.htm"
driver = webdriver.Chrome("../DATA/chromedriver")
driver.get(melon_url)

# 최신음악 메뉴
new_song_button = driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[2]/a')
new_song_button.click()
time.sleep(1)

# 최신앨범 탭
new_album_button = driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[2]/div/ul/li[2]/a')
new_album_button.click()
time.sleep(1)

# 변수명
# new album title list : nat_list
# new album artist list : naa_list
# new album heart cnt list : nahc_list
# new album song cnt list : nasc_list
# new album release date list : nard_list

page_cnt = 1
nat_list = []
naa_list = []
nahc_list = []
nasc_list = []
nard_list = []
country_list = []

# 국내 최신앨범 앨범명, 아티스트, 좋아요수, 수록곡수, 발매일 가져오기
print("국내 최신 앨범 크롤링 시작")
while True :
    for page in range(1, 11, 1) :
        for num in range(1, 21, 1) :
            album_title = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[1]/a')
            for title in album_title :
                nat_list.append(title.text)
            album_artist = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[1]/span[2]')
            for artist in album_artist :
                naa_list.append(artist.text)
            album_heart = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[2]/button/span[2]')
            for heart in album_heart :
                if "," in heart.text :
                    nahc_list.append(int(heart.text.replace(",", "")))
                else :
                    nahc_list.append(int(heart.text))
            song_cnt = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[2]/span[2]')
            for song_num in song_cnt :
                nasc_list.append(song_num.text)
            release_date = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[2]/span[1]')
            for date in release_date :
                nard_list.append(date.text)
                country_list.append("국내")
            
                
        try :
            page_button = driver.find_element_by_xpath(f'//*[@id="pageObjNavgation"]/div/span/a[{page}]')
            page_button.click()
            time.sleep(2)
        except :
            break
        finally :
            print(f"{page_cnt}page까지 완료")
        page_cnt += 1

    if page_cnt == 10 :
        next_button = driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/a')
        next_button.click()
        time.sleep(2)
    elif page_cnt == 20 :
        next_button = driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/a[2]')
        next_button.click()
        time.sleep(2)
    else :
        break
    page_cnt += 1

print("new album title list length :", len(nat_list))
print("new album artist list length :", len(naa_list))
print("new album heart cnt list length :", len(nahc_list))
print("new album song cnt list length :", len(nasc_list))
print("new album release date list length :", len(nard_list))
print("country list length :", len(country_list))

# 해외 button 클릭
foreign_button = driver.find_element_by_xpath('//*[@id="conts"]/div[2]/ul/li[2]/a')
foreign_button.click()
time.sleep(1)

# page 번호 초기화
page_cnt = 1 

# 해외 최신앨범 앨범명, 아티스트, 좋아요수, 수록곡수, 발매일 가져오기
print("해외 최신 앨범 크롤링 시작")
while True :
    for page in range(1, 11, 1) :
        for num in range(1, 21, 1) :
            album_title = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[1]/a')
            for title in album_title :
                nat_list.append(title.text)
            album_artist = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[1]/span[2]')
            for artist in album_artist :
                naa_list.append(artist.text)
            album_heart = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[2]/button/span[2]')
            for heart in album_heart :
                if "," in heart.text :
                    nahc_list.append(int(heart.text.replace(",", "")))
                else :
                    nahc_list.append(int(heart.text))
            song_cnt = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[2]/span[2]')
            for song_num in song_cnt :
                nasc_list.append(song_num.text)
            release_date = driver.find_elements_by_xpath(f'//*[@id="frm"]/div/ul/li[{num}]/div[2]/div[2]/span[1]')
            for date in release_date :
                nard_list.append(date.text)
                country_list.append("해외")
            
                
        try :
            page_button = driver.find_element_by_xpath(f'//*[@id="pageObjNavgation"]/div/span/a[{page}]')
            page_button.click()
            time.sleep(2)
        except :
            break
        finally :
            print(f"{page_cnt}page까지 완료")
        page_cnt += 1

    if page_cnt == 10 :
        next_button = driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/a')
        next_button.click()
        time.sleep(2)
    elif page_cnt == 20 :
        next_button = driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/a[2]')
        next_button.click()
        time.sleep(2)
    else :
        break
    page_cnt += 1

print("new album title list length :", len(nat_list))
print("new album artist list length :", len(naa_list))
print("new album heart cnt list length :", len(nahc_list))
print("new album song cnt list length :", len(nasc_list))
print("new album release date list length :", len(nard_list))
print("country list length :", len(country_list))

# 앨범 정보 DataFrame 생성
album_dict = {"곡 제목" : nat_list, "아티스트" : naa_list, "좋아요" : nahc_list, "수록곡 수" : nasc_list, "발매일" : nard_list, "국가" : country_list}
album_df = pd.DataFrame(album_dict)
print(album_df)
album_df.to_csv("./" + datetime.today().strftime("%Y_%m_%d") + "_최신앨범정보.csv", index = False)