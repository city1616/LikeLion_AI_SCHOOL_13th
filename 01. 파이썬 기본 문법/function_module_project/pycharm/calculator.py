# 계산기 프로그램, 사칙연산, 추가연산, 0 초기

class Cal :
    result = 0

    # 생성자 메서드
    def __init__(self):
        self.result = 0

    def cal(self, num1, op, num2) :
        if op == "+" :
            self.result = num1 + num2
            return self.result
        elif op == "-" :
            self.result = num1 - num2
            return self.result
        elif op == "*" :
            self.result = num1 * num2
            return self.result
        elif op == "/" :
            self.result = num1 / num2
            return self.result
        elif op == "//" :
            self.result = num1 // num2
            return self.result
        elif op == "%" :
            self.result = num1 % num2
            return self.result
        elif op == "**" :
            self.result = num1 ** num2
            return self.result
        else :
            return "Error"

    def Czero(self):
        self.result = 0
        return self.result

c1 = Cal()

for i in range(5) :
    val1, op, val2 = input("수식 입력 : ").split()
    result = c1.cal(int(val1), op, int(val2))
    print("결과 :", result)

print("초기화 : ", c1.Czero())
'''
val1 = int(input("val1 : "))
op = input("operator : ")
val2 = int(input("val2 : "))
'''