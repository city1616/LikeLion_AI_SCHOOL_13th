# Step 1. 학번 계산기
# 목표 : 나와 동료의 학번을 입력하고, 호칭을 정해봅시다.
# Step 1. 나와 동료의 학번을 입력받아서 비교 해봅시다.
# Step 2. 동료의 학번이 나와 같다면, "앗! 동기네요"라고 출력 해봅시다.
# Step 3. 동료의 학번에 따라 호칭을 다르게 인사 해봅시다. e.g. 안녕하세요(후배님 / 동기님 / 선배님)

# Step 1. 조건
# 결과 -> True / False
# 연산자 -> ==, !=, <, >, <=, >=
# a == b : a와 b가 같니?
# a != b : a와 b가 다르니?
# a < b  : a가 b보다 작니?
# a > b  : a가 b보다 크니?
# a <= b : a가 b보다 작거나 같니?
# a >= b : a가 b보다 크거나 같니?
'''
myGrade = 10
yourGrade = 15
print(myGrade == yourGrade)		# False
print(myGrade != yourGrade)		# True
'''
myGrade = int(input("학번을 입력하세요 : "))
yourGrade = int(input("학번을 입력하세요 : "))
print(myGrade != yourGrade)		# 다르면 True, 같으면 False
print(myGrade == yourGrade)
print(myGrade > yourGrade)
print(myGrade >= yourGrade)

# Step 2. if문
# 버스 카드에 잔액이 부족하니? 
# True : 내려서 뛰어간다
# False : 편안히 버스를 타고 간다
myGrade = int(input("학번을 입력하세요 : "))
yourGrade = int(input("학번을 입력하세요 : "))

if myGrade == yourGrade :		# 들여쓰기 되있는 부분만 if문으로 인식
	print("앗! 동기네요!")
	print("반갑습니다.")
print("누구세요?")					# 같을 경우 print문 세개가 출력됨, 다를 경우 마지막 print문만 출력됨
								# 마지막 print문은 if문에 포함되어있지 않음
if myGrade != yourGrade :
	print("앗! 동기네요!")
	print("반갑습니다.")
print("누구세요?")					# 다를 경우 print문 세개가 출력됨, 같을 경우 마지막 print문만 출력됨

# if else문
# if 조건 : -> True일 때 실행될 코드
# else :   -> False일 때 실행될 코드
myGrade = int(input("학번을 입력하세요 : "))
yourGrade = int(input("학번을 입력하세요 : "))

if myGrade == yourGrade :
	print("앗! 동기네요!")
else :
	print("앗! 동기가 아니네요!")

# Step 3. if elif else문
# if 조건 :    -> True일 때 실행될 코드
# elif 조건 :  -> True일 때 실행될 코드
# else :      -> False일 때 실행될 코드
myGrade = int(input("학번을 입력하세요 : "))
yourGrade = int(input("학번을 입력하세요 : "))

if myGrade == yourGrade :
	print("안녕하세요 동기님!")
elif myGrade > yourGrade :
	print("안녕하세요 선배님!")
elif myGrade < yourGrade :
	print("안녕하세요 후배님!")
else :
	print("누구세요?")

# 지금 주문 되나요?
# if + list
orders = ["짜장", "짬뽕", "탕수육"]
food = input("먹고 싶은 메뉴를 입력해주세요 : ")
if food in orders :				# food가 orders 안에 존재하면 True
	print("주문할 수 있습니다.")
else :
	print("주문할 수 없습니다.")

# if + dictionary
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
food = input("먹고 싶은 메뉴를 입력해주세요 : ")
if food in menu :
	print("주문 가능")
	print(menu[food], "원 입니다.")
else :
	print("주문 불가")












