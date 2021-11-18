# # 2021_09_02_05
# data eda 를 수행하는 모듈을 불러오기

import pandas as pd

def basicinfo(data) :
    # 행과 열
    print( data.describe() )

    # 기본 정보
    print( data.info() )