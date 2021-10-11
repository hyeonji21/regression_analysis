# 앤스콤 데이터 집합 불러오기
import notebook as notebook
import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")
print(anscombe)
print(type(anscombe))

# 그룹별 데이터 추출
dataset_1 = anscombe[anscombe['dataset']=='I']
dataset_2 = anscombe[anscombe['dataset']=='II']
dataset_3 = anscombe[anscombe['dataset']=='III']
dataset_4 = anscombe[anscombe['dataset']=='IV']

# 기본틀 만들기
fig = plt.figure()

# 격자 그리기
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2 ,3)
axes4 = fig.add_subplot(2, 2, 4)

# 그래프 채우기
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

# 소제목 달기
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

# 제목 달기
fig.subtitle('Anscombe Data')

#레이아웃 조절
fig.tight_layout

fig