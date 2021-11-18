# 2021_09_02_06
# enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아
#             인덱스 값을 포함하는 enumerate 객체를 돌려준다.

a = ['a', 'b', 'c']
print(enumerate(a))
print(list(enumerate(a)))

for idx, val in enumerate(a) :
    print(idx, val)

b = ('a', 'b', 'c')
print(enumerate(b))
print(tuple(enumerate(b)))

for idx, val in enumerate(b) :
    print(idx, val)

str1 = "hello"
print(enumerate(str1))
print(list(enumerate(str1)))

for idx, val in enumerate(str1) :
    print(idx, val)