# 치과 데이터를 분석해 신설 치과, 폐업 치과 분석

import pandas as pd
from datetime import datetime
import time
import os

base_path = r'/Users/seungwoomun/Documents/Github/LikeLion_AI_SCHOOL_13th/개인 프로젝트/'

now = datetime.now()
current_time = now.strftime("%Y_%m_%d_%H")

file_name = current_time + "_병원·약국찾기.csv"

file_path = os.path.join(base_path, file_name)

print(file_name)

p_data = pd.read_csv("./" + file_name, encoding = "utf-8")

print("data shape :", p_data.shape)