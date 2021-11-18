# 2021_09_02_04
# 함수 < 클래스 < 모듈(함수, 변수, 클래스) < 라이브러리(패키지)

# 모듈이름 : module01
# 앞으로이동
# 뒤로 이동

# x = 0 # 현재 위
loc = [0, 0]

def forward_move(move) :
    # print("현재 x 위치 : ", loc[0])
    print(f"앞으로 {move}칸 이동")
    loc[0] += move
    return loc[0] + move

def backward_move(move) :
    # print("현재 x 위치 : ", loc[0])
    print(f"로 {move}칸 이동")
    loc[0] -= move
    return loc[0] - move