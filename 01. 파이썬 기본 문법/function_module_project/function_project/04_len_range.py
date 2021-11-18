# 2021_09_02_06
# len : len(s)는 입력값 s의 길이(요소의 전체 개수)를 돌려준다.

a = ['a', 'b', 'c']
b = (1, 2, 3, 4)
c = "hello world"

print(len(a))
print(len(b))
print(len(c))

print(list(range(0, 10, 1)))

# isalpha() : 알파벳으로 구성되어 있으면 True를 반환, 다른 문자가 하나라도 포함되면 False 반환
print("python".isalpha())
print("P".isalpha())
print("".isalpha())
print("가나다".isalpha())

# 6-6 어떤 값또는 문자열을 입력받아서, 알파벳이 몇글자인지 확인해 보기
str1 = input("입력 : ")
result = []
num = []
space = []

all_str = []
for i in range(65, 91, 1) :
    all_str.append(chr(i))
for i in range(97, 123, 1) :
    all_str.append(chr(i))

# isalpha() -> 한글도 알파벳으로 구분
for i in str1 :
    if i in all_str :
        result.append(i)
    elif i.isnumeric() :
        num.append(i)
    elif i.isspace() :
        space.append(i)


print(f"알파벳 : {result}\n알파벳의 개수 : {len(result)}")
print(f"숫자 : {num}\n숫자의 개수 : {len(num)}")
print(f"공백 : {space}\n공백의 개수 : {len(space)}")