import time
import random

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

# 음식 추가
while True :
	print(lunch)
	item = input("음식을 추가 해주세요 : ")						# 사용자 입력
	if(item == "q") :
		break
	else :
		lunch.append(item)

print(lunch)
	
'''
차집합 - 집합끼리 연산 가능, 집합과 문자열 연산을 했을 경우 오류 발생 -> 문자열을 집합으로 바꿔야함

set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"
print(set_lunch - set([item]))				# 짜장면을 제외한 나머지 데이터 출력
set_lunch = set_lunch - set([item])			# set_lunch에서 짜장면이 삭제됨
print(set_lunch)							# 짜장면이 삭제됨
'''

# 음식 삭제
set_lunch = set(lunch)
while True :
	print(set_lunch)
	item = input("음식을 삭제해주세요 : ")
	if item == "q" :
		break
	else :
		set_lunch = set_lunch - set([item])

# 최종 음식 출력
print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1) 						# 1초 쉬기
print("4")
time.sleep(1) 						# 1초 쉬기
print("3")
time.sleep(1) 						# 1초 쉬기
print("2")
time.sleep(1) 						# 1초 쉬기
print("1")
time.sleep(1) 						# 1초 쉬기

print(random.choice(list(set_lunch)))						# 집합을 리스트로 변환
