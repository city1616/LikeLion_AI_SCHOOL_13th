# module01.py
x = 0 # 현재 위

def forward_move(move) :
    print("현재 x 위치 : ", x)
    print(f"앞으로 {move}칸 이동")
    return x + move

def backward_move(move) :
    print("현재 x 위치 : ", x)
    print(f"로 {move}칸 이동")
    return x - move

# module02.py
y = 0

def left_move(move) :
    print("현재 y 위치 : ", y)
    print(f"앞으로 {move}칸 이동")
    return y + move

def right_move(move) :
    print("현재 y 위치 : ", y)
    print(f"앞으로 {move}칸 이동")
    return y - move

# module_test01.py
import module01
import module02

final_loc = []
final_loc.append(module01.forward_move(10))
final_loc.append(module02.left_move(10))

print("현재 x 위치 : ", final_loc[0])
print("현재 y 위치 : ", final_loc[1])