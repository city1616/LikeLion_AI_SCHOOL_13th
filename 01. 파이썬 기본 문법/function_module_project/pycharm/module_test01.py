# 2021_09_02_04

import module01
import module02

# final_loc = []

# final_loc.append(module01.forward_move(10))
# final_loc.append(module02.left_move(10))

# print("현재 x 위치 : ", final_loc[0])
# print("현재 y 위치 : ", final_loc[1])
# print(final_loc)

def update_loc() :
    print(module01.loc)

for i in range(3) :
    move = int(input("이동 횟수 : "))
    module01.forward_move(move)
    module02.left_move(move)
    update_loc
