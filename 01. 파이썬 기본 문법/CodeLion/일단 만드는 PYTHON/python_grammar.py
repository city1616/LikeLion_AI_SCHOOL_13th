import random
import time

# print(random.choice(["된장찌개", "피자", "제육볶음"])) # ["된장찌개", "피자", "제육볶음"] -> list

# DRY - Don't Repeat Yourself(반복문)
# 대신 반복하기
for i in range(30) :
	print(random.choice(["된장찌개", "치킨", "떡볶이", "라면", "감자튀김"]))
	print("이 문장도 반복?")


while True :         # ctrl + c, break : 무한루프 종료
	print(random.choice(["된장찌개", "치킨", "떡볶이", "라면", "감자튀김"]))
	print("이 문장도 반복?")
	time.sleep(1) # 1초동안 쉬기

# 데이터 상자 만들기
lunch = random.choice(["된장찌개", "피자", "제육볶음"])
lunch = "냉장고" # 이전 데이터는 지워지고 새로운 데이터가 들어감
dinner = random.choice(["김밥", "쫄면", "돈까스"])
print(lunch)

# Dictionary
information = {"고향" : "수원", "취미" : "영화관람", "좋아하는 음식" : "국수"}
print(information)
print(information.get("취미")) # 영화관람 출력

information = {"특기" : "피아노", "사는곳" : "서울"}
print(information.get("특기"))
print(information.get("사는곳"))

# List와 Dictionary
information = {"고향" : "수원", "취미" : "영화관람", "좋아하는 음식" : "국수"}
foods = ["된장찌개", "피자", "제육볶음"]
print(information.get("취미"))
information["특기"] = "피아노"		# 특기 추가
information["사는곳"] = "서울"		# 사는곳 추가
del information["좋아하는 음식"] 	# 좋아하는 음식 삭제
print(information)				# 특기와 사는곳 추가, 좋아하는 음식 삭제
print(len(information)) 		# 길이 출력, 4 출력됨
information.clear() 			# dictionary 초기화
print(information)				# {} 출력됨

print(foods[0]) 				# foods 리스트의 맨 처음 데이터가 출력됨, 된장찌개
print(foods[1]) 				# 피자
print(foods[2])					# 제육볶음
print(foods[3])					# list index out of range error
print(foods[-1]) 				# foods 리스트의 제일 마지막 데이터가 출력됨, 제육볶음
print(foods[-2])				# 피자
foods.append("김밥") 				# foods 리스트에 김밥 추가
print(foods) 					# 김밥 추가됨
del foods[1] 					# 피자 삭제
print(foods)					# 피자 삭제됨

# 끝까지 반복하기
for i in range(30) :
	print(i)

foods = ["된장찌개", "피자", "제육볶음"]

print(foods)
print(foods[0])
print(foods[1])
print(foods[2])

for i in range(3) : # i = 0, 1, 2
	print(foods[i])

for i in foods :  	# i = "된장찌개", "피자", "제육볶음"
	print(i)

information = {"고향" : "수원", "취미" : "영화관람", "좋아하는 음식" : "국수"}
for x, y in information.items() :
	print(x)
	print(y)

# 집합 알아보기
# 집합 - 순서와 중복이 없다. 
# 리스트 - 순서와 중복이 있다. 
# 1. 합집합 연산 (중복제거)
# 2. 차집합 연산 (공통부분 제거)
# 3. 교집합 연산 (공통부분)
foods = ["된장찌개", "피자", "제육볶음"]
foods_set1 = set(foods) 						# 집합 생성
foods_set2 = set(["된장찌개", "피자", "제육볶음"])	# 집합 생성
print(foods_set1)
print(foods_set2)

# 집합 사용하기
foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
foods_set = set(foods) 							# 집합 생성
print(foods)									# 리스트 출력
print(foods_set)								# 집합 출력(중복 제거됨, 순서 없음)

menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 | menu2 						# 합집합 (중복 제거됨)
menu3 = menu1 & menu2 						# 교집합 (겹친 메뉴 출력)
menu3 = menu1 - menu2						# 차집합 (menu1에서 겹친 메뉴 제외)
print(menu3)

# 만약에(if문)
import random

food = random.choice(["된장찌개", "피자", "제육볶음"])

print(food)
if(food == "제육볶음") :
	print("곱배기 주세요")
else :
	print("그냥 주세요")
print("종료")


# 함수 알아보기
def make_dolcelatte() :
	print("1. 얼음을 넣는다.")
	print("2. 연유를 30ml 넣는다.")
	print("3. 찬 우유를 넣는다.")
	print("4. 에스프레소샷을 넣는다.")

def make_blueberry_smoothie() :
	print("1. 블루베리 20g을 넣는다.")
	print("2. 우유 300ml를 넣는다.")
	print("3. 얼음을 넣는다.")
	print("4. 믹서기에 간다.")

def make_simple_latte() :
	print("1. 커피를 넣는다.")
	print("2. 우유를 넣는다.")
	print("3. 신나게 섞는다.")

make_simple_latte()
make_blueberry_smoothie()
make_dolcelatte()
make_dolcelatte()














