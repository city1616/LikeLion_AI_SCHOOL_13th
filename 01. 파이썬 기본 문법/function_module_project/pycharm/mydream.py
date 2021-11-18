# 2021_09_02_05
# 변수, 클래스, 함수
likecolor = 'purple'

def yourdream(a) :
    return a * 1

class myact :
    height = 175
    def walk(self) :
        action = "걷는다"
        return action

    def haha(self) :
        action = "웃는다"
        return action

    def coding(self) :
        action = "코딩하기"
        return action

    def run(self) :
        action = "뛰기"
        return action

# python mydream.py 직접 실행할 경우 __name__ -> __main__
# import 로 불러올 경우 __name -> 모듈 파일명
if __name__ == "__main__" :
    print("mydream 시작")
    print(__name__)     # __main__
else :
    print(__name__)     # mydream