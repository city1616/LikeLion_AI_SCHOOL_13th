# 2021_09_02_06
# 절대값 구하기

print(abs(3))
print(abs(-13))

# 6-2 실습 - 두 개의 값을 입력받아서, 값의 차이의 절대값를 구하는 프로그램을 만들어보자.
def two_abs(a, b) :
    return abs(a - b)

num1 = int(input("val1 : "))
num2 = int(input("val2 : "))
result = two_abs(num1, num2)
print(f"결과 : {result}")
