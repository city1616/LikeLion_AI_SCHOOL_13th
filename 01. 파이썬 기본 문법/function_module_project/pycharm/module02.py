# 2021_09_02_04

# 모듈이름 : module02
# 왼쪽으로 이동
# 오른쪽으로 이동
import module01

def left_move(move) :
    # print("현재 y 위치 : ", module01.loc[1])
    print(f"앞으로 {move}칸 이동")
    module01.loc[1] += move
    return module01.loc[1] + move

def right_move(move) :
    # print("현재 y 위치 : ", module01.loc[1])
    print(f"앞으로 {move}칸 이동")
    module01.loc[1] -= move
    return module01.loc[1] - move