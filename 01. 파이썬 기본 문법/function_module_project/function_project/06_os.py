# 2021_09_02_07
# os : 환경변수나 디렉터리, 파일 등의 os자원을 제어할 수 있게 해 주는 모듈

import os

# 현재 작업 위치
print(os.getcwd())

# 현재 작업 위치의 파일 보기
print(os.listdir())

# 7-2 (추가) 해당 위치의 파일이 몇개 있고, 그리고 원하는 파일이 있는지 확인 유무.
print(f"현재 위치의 파일 또는 폴더의 개수 : {len(os.listdir())}")
file_name = input("찾고자 하는 파일명 : ")

if file_name in os.listdir() :
    print(f"{file_name} 파일 있음")
else :
    print(f"{file_name} 파일 없음")

# 7-3 (추가) .py파일이 몇개인지.
cnt_py = 0
cnt_ipynb = 0
for i in os.listdir() :
    if i[-3:] == '.py' :    # if ".py" in file:
        cnt_py += 1
    elif i[-6:] == '.ipynb' :
        cnt_ipynb += 1
print(f".py 파일의 개수 : {cnt_py}")
print(f".ipynb 파일의 개수 : {cnt_ipynb}")