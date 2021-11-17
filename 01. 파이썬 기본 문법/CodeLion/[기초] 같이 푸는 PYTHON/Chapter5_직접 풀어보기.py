# Step 1. 별이 빛나는 밤
# * 찍기
print("*")					# *

# * 세로로 5개 찍기
for i in range(5) :
	print("*")				# *
							# *
							# *
							# *
							# *

# * 가로로 5개 찍기
for i in range(5) :
	print("*", end = "")	# *****

# *****
# *****
# *****
# *****
# *****
for i in range(5) :
	for x in range(5) :
		print("*", end = "")
	print()

# *
# **
# ***
# ****
# *****
for i in range(5) :
	for x in range(i + 1) :
		print("*", end = "")
	print()

# Step 2. 줄 바꿔 출력하기
# 변수 x에 숫자를 입력받아 1부터 x까지의 숫자 모두 출력하기
# ex) x = 5 -> 1 2 3 4 5
x = int(input("숫자를 입력해주세요 : "))
for i in range(x) :
	print(i + 1)			# 5 -> 1 2 3 4 5

# 5 -> 5 4 3 2 1
x = int(input("숫자를 입력해주세요 : "))
for i in range(x, 0, -1) :
	print(i)

# 30 -> 1 2 3 4 5 6 7 8 9 10
# 		11 12 13 14 15 16 17 18 19 20
# 		21 22 23 24 25 26 27 28 29 30
x = int(input("숫자를 입력해주세요 : "))
for i in range(x) :
	print(i + 1, end = " ")
	if (i + 1) % 10 == 0 :
		print()

# Step 3. 오늘의 당첨번호
# 로또 번호 생성기
# 로또 번호를 선택하는 방법
# 1. 1부터 45까지 숫자가 하나씩
# 2. 이 중 아무거나 6개를 선택
# random -> 임의의 어떠한 난수를 만들어주는 기능(아무거나)
# random.sample(랜덤범위, 개수)
import random

randomNumber = random.sample(range(1, 100), 10)
print(randomNumber)				# 1부터 99 중 임의의 10개를 뽑아 리스트로 반환


randomNumber = random.sample(range(1, 51), 3)
print(randomNumber) 			# 1부터 50 중 임의의 3개를 뽑아 리스트로 반환

# 문제
# 1. 사용자에게 로또를 몇 개 살 건지 숫자 입력
# 2. 1부터 45까지 숫자 중 6개를 랜덤으로 뽑기
# 3. 사용자에게 입력받은 개수만큼 2번을 뽑기
# 4. 오름차순으로 정렬해서 출력하기
import random

cnt = int(input("구매할 로또 개수를 입력하세요 : "))
for i in range(cnt) :
	randomNumber = random.sample(range(1, 46), 6)
	randomNumber.sort()
	print(randomNumber)






















