# Step 1. 별이 빛나는 밤 - 해설
# *****
for i in range(5) :
	print("*", end = "")	# *****

print("*" * 5) 				# *****

# *****
# *****
# *****
# *****
# *****
for x in range(5) :
	print("*" * 5)

# *
# **
# ***
# ****
# *****
for x in range(5) :
	print("*" * (x + 1))

# Step 2. 줄 바꿔 출력하기 - 해설
# 5 -> 5 4 3 2 1
x = int(input("숫자를 입력하세요 : "))
for i in range(x, 0, -1) :
	print(i)

# x = 30
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30
x = int(input("숫자를 입력하세요 : "))
for i in range(x) :
	if i % 10 == 0 :
		print()
	print(i + 1, end = "\t")
print()

# Step 3. 오늘의 당첨번호 - 해설
# 문제
# 1. 사용자에게 로또를 몇 개 살 건지 숫자 입력
# 2. 1부터 45까지 숫자 중 6개를 랜덤으로 뽑기
# 3. 사용자에게 입력받은 개수만큼 2번을 뽑기
# 4. 오름차순으로 정렬해서 출력하기
import random

count = int(input("로또를 몇개 구매하시겠습니까? "))
for i in range(count) :
	lotto = random.smaple(range(1, 46), 6)
	lotto.sort()
	print(lotto)
print("로또 종료")