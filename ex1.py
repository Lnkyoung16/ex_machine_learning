import pandas as pd

#폴더이름(폴더가 다를 때)/파일이름 파일 읽기
data = pd.read_csv("data/train.csv")

#데이터 요약.
data.describe()

#데이터에서 2가지 이상의 기준 열람
data[['Sex','Survived']]

#분석한 결과 변수에 저장.
data_sex = data['Sex'] == "male"

#분석된 참거짓을 숫자로 변환.
data_sex = data_sex.astype(int).values

#숫자 총합.
data_sex.value_counts()

#Survived 가 1인 데이터만 보여줌.
data[data['Survived'] == 1]

#생존한 사람들의 성별만 보여줌.
survived_data = data[data['Survived'] == 1]['Sex'].value_counts()

import matplotlib.pyplot as plt

#선그래프.
plt.plot(survived_data)

#원그래프.
plt.pie(survived_data)

#그래프 이름 짓기.
plt.title("survived_data")

survived_data.index

#label 인덱스를 써서 표기해라.
#autopct= 퍼센트 표기.'%.(소수점몇자리)f%%'
plt.pie(survived_data, labels = survived_data.index, autopct='%.1f%%')

#그래프 이미지로 저장하기.
plt.savefig("plot/survived_sex.png")

survived_pclass_data = data[data['Survived'] == 1]['Pclass'].value_counts()
data['Pclass'].value_counts()
plt.pie(survived_pclass_data)
plt.title("survived_pclass_data")
plt.pie(survived_pclass_data, labels=survived_pclass_data.index, autopct='%.1f%%')
plt.savefig("plot/survived_pclass_data.png")

#
data['Age'].mean()

data[data['Sex'] == 'female'][data['Survived'] == True]['Age'].mean()
data[data['Sex'] == 'male']['Age'].mean()