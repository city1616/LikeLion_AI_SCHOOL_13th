# # 2021_09_02_05
# data eda 를 수행하는 모듈을 불러오기
import myeda
import seaborn as sns

tips = sns.load_dataset("tips")

myeda.basicinfo(tips)