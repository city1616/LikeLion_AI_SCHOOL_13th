# 친구의 이름을 입력받고, "이름"아 안녕! 이라고 출력해 봅시다.
name = input("이름을 입력해주세요 : ")
print(name + "씨 안녕!!")

# 친구와 먹은 메뉴의 가격을 더해서, 총 금액을 계산해 출력해 봅시다.
# input -> 글짜로 저장됨(string)
# int() -> int(숫자)형으로 타입 변환(형변환)
food1 = input("내가 먹은 음식의 가격 : ")
food2 = input("친구가 먹은 음식의 가격 : ")

food1 = int(food1)
food2 = int(food2)

print(food1 + food2)

# 연산자
# +, -, *, /
print(10 + 20)		# 30
print(10 - 20)		# -10

월세 = int(input("월세를 입력해주세요 : "))
관리비 = int(input("관리비를 입력해주세요 : "))

print(월세 + 관리비)
print(월세 - 관리비)
print((월세 + 관리비) * 12)
print(월세 / 관리비)

# 중식당 주문(list)
# 중식당에서 주문을 해봅시다. 나열한 순서대로 주문합니다.
# Step 1. 비어있는 주문서(list)를 만들어 "orders"라는 이름을 지어주세요.
# Step 2. 순서대로 "짜장", "짬뽕", "탕수육"을 넣어주세요.
# Step 3. "냉면"을 첫 번째로 추가해주세요.
# Step 4. 생각해보니 "짬뽕"이 안땡겨요. 삭제해주세요.
# Step 5. 주문서에 총 몇 개의 음식이 있나요?

# 각 data를 요소(elements) 라고 부름
# 각 data는 index로 구분됨
orders = ["짜장", "짬뽕", "탕수육"] 			
print(orders[0])							
print(orders)

number = [10, 20, 30, 40, 50]
print(number)

# list[]에 data 추가하기
# append() -> 이어 붙이기
orders.append("냉면")
print(orders) 				# ["짜장", "짬뽕", "탕수육", "냉면"]

# insert() -> index 위치에 값 추가
orders.insert(1, "냉면")
print(orders) 				# ["짜장", "냉면", "짬뽕", "탕수육"]

orders.insert(3, "양장피")
print(orders) 				# ["짜장", "짬뽕", "탕수육", "양장피"]

# list[] data 삭제하기
# del
del orders[1]
print(orders)				# ["짜장", "탕수육"]

# remove()
orders.remove("짬뽕")
print(orders)				# ["짜장", "탕수육"]

# Step 5. 주문서에 총 몇 개의 음식이 있나요?
# list[]의 길이 구하기 -> len()
orders = ["짜장", "짬뽕", "탕수육"]
print(len(orders))			# 3

name = "안녕하세요 코드라이언입니다."
print(len(name))			# 15

# 숫자 리스트
# 숫자로 구성된 list를 만들어 봅시다.
# Step 1. 20, 40, 50, 10, 30 으로 이러우진 이름이 num인 list를 만들어 주세요.
# Step 2. list 안의 숫자들의 전체 합을 출력해주세요.
# Step 3. list 안의 숫자들의 평균을 출력해 주세요.
# Step 4. 가장 큰 값과 작은 값을 각각 출력해 주세요.

# Step 1.
num = [20, 40, 50, 10, 30]
print(num)

# Step 2.
# sum() -> 리스트 숫자 데이터들의 총합
add = sum(num) 				# -> add = num[0] + num[1] + num[2] + num[3] + num[4]
print(add)

# Step 3.
# 평균 = (전체의 합) / 전체 개수
num = [20, 40, 50, 10, 30]
print(sum(num) / len(num)) 	# 30.0

# Step 4.
# max() -> 최대값
# min() -> 최소값
num = [20, 40, 50, 10, 30]
print("최대값 : ", max(num))	# 50
print("최소값 : ", min(num))	# 10

# 중식당 메뉴판(dictionary)
# 중식당 메뉴판을 만들어 봅시다.
# Step 1. 비어있는 메뉴판(dictionary)을 만들어 "menu"라는 이름을 지어 주세요.
# Step 2. 메뉴판에 음식 이름과 가격을 넣어 메뉴판을 만들어 주세요.
# Step 3. 새로운 메뉴 "냉면"을 메뉴판에 추가해주세요.
# Step 4. "짬뽕"의 가격이 얼마죠? "짬뽕"의 가격을 출력해 주세요.
# Step 5. 생각보다 탕수육이 비싼 것 같아요. 탕수육의 가격을 8500원으로 변경해주세요.
# Step 6. 준비해둔 "짜장" 재료가 다 떨어졌어요. "짜장"을 메뉴판에서 삭제해 주세요.
# Step 7. 완성된 메뉴판 전체를 출력해 주세요.

# Step 1. 
menu = {}
print(menu)					# {}

# Step 2.
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
prnt(menu)

family = {"아빠" : 45, "엄마" : 49, "나" : 22}
print(family)

# Step 3.
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
menu["냉면"] = 6000			# "냉면" : 6000 dictionary에 추가
print(menu)

# Step 4.
# dictionary 출력 -> print(dict["key"])
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
print(menu["짬뽕"])						# 5000
print(menu["탕수육"], menu["짜장"]) 		# 9000 4000

# Step 5.
# dictionary value 변경
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
menu["탕수육"] = 8500
print(menu["탕수육"])						# 8500
menu["짜장"] = 4500
print(menu["짜장"]) 						# 4500

# Step 6.
# dictionary 삭제 -> del
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
del menu["짜장"]
print(menu) 							# {"짬뽕" : 5000, "탕수육" : 9000}
del menu["짬뽕"]
del menu["탕수육"]
print(menu)								# {}

# Step 7.
# dictionary 출력 -> print(dictionary)
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
print(menu)								# {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

menu["냉면"] = 6000		
print(menu)								# {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000, "냉면" : 6000}

print(menu["짬뽕"]) 						# 5000

menu["탕수육"] = 8500
print(menu["탕수육"]) 					# 8500

del menu["짜장"]
print(menu)								# {짬뽕" : 5000, "탕수육" : 9000, "냉면" : 6000}











