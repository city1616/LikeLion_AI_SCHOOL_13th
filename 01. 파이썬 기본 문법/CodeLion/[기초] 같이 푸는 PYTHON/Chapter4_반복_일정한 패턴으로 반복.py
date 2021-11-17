# Step 1. 무한반복
# while
# ~하는 동안에 -> 조건이 True인 동안에 계속 실행
# while 조건 : True일 때 실행될 코드
while 10 < 90 : 			# 무한루프(무한반복)
	print("True")			# 탈출 방법 -> Ctrl + c

# Step 2. 순차출력
i = 0
while i < 6 :
	# print("True")
	print(i)				# 0 ~ 5 출력
	i = i + 1

a = 5
while a >= 0 :
	print(i)				# 5 ~ 0 출력
	i = i - 1

# Step 3. 탈출하기
# break -> 반복문 탈출
i = 0
while True :
	print(i)				# 0 ~ 2 출력
	i = i + 1
	if i >= 3 :
		print("if문 동작")
		break
print("반복문 종료!")

# Step 4. 건너뛰기
# continue -> 반복문 위로 올라감 / continue 아래의 코드는 실행하지 않음
i = 0
while i < 10 :
	i = i + 1
	if i % 2 == 0 :			# 2로 나누었을 때 나머지가 0이면 True / 짝수
		continue			# 짝수일 경우 아래 print문은 실행하지 않고 반복문의 맨 처음으로 올라감
	print(i)				# 1 3 5 7 9
print("반복 종료!")

# Step 5. x까지 반복
# for in
# for 변수 in 시퀀스 : 실행될 코드
# 시퀀스 -> 어떠한 순서를 가지고 있는 데이터의 집합, list, tuple
# for x in [10, 20, 30] : print(x) -> 10, 20, 30 출력

# Step 6. x부터 y까지 반복
for x in [10, 20, 30] :
	print("안녕하세요") 		# 3번 출력

# range() -> 범위 지정
# range(시작숫자, 종료숫자, 스텝) -> 시작숫자와 스텝은 생략 가능
# range(종료숫자) -> 0 ~ 종료숫자까지 1씩 증가하면서 반복
# range(시작숫자, 종료숫자) -> 시작숫자 ~ 종료숫자까지 1씩 증가하면서 반복
for x in range(100) :
	print("안녕하세요") 		# 100번 출력

for x in range(10) :
	print(x) 				# 0 ~ 9 출력

for x in range(10, 20) :
	print(x) 				# 10 ~ 19 출력

# Step 7. x부터 y까지 z만큼 반복
# range(시작숫자, 종료숫자, 스텝) -> 시작숫자 ~ 종료숫자까지 스텝만큼 증가하면서 반복
for x in range(10, 20, 2) :
	print(X) 				# 10, 12, 14, 16, 18 출력

for x in range(3, 31, 3) :
	print(x)				# 3, 6, 9, 12, 15, 18, 21, 24, 27, 30

for x in range(2, 31, 2) :
	print(x) 				# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30

# Step 8. 100까지의 합
# 1부터 100까지 모두 더하는 프로그램
result = 0
for x in range(1, 101) :
	result = result + x
print(result)				# 5050

# 1부터 10까지 모두 곱하는 프로그램
result = 1
for x in range(1, 11) :
	result = result * x
print(x)					# 3628800





















