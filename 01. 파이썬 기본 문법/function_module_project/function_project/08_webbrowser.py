# 2021_09_02_07
# time, webbrowser 실습
# browser 실행 후 2초 쉬기
import webbrowser
import time

web = ["http://google.com",
       "http://naver.com",
       "http://youtube.com",
       "http://netflix.com",
       "http://apple.com"]

for i in web :
    webbrowser.open(i)
    time.sleep(2)
