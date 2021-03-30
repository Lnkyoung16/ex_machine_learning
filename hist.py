import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("data/train.csv")
data = data.dropna()

#data[['Age" , "SibSp']]
num_var = ['Age', 'SibSp', 'Parch', 'Fare', 'Pclass']
#cat_var = ['Survived','Pclass','Sex','Ticket','Cabin','Embarked']
df_num = data[num_var]
#df_cat = data[cat_var]

data["Age"]

df_num.columns[0]
df_num.index
df_num.Age
df_num["Age"]

for r in num_var:
    plt.hist(df_num[r])
    plt.title(r)
    plt.savefig("plot/hist/survived_" + r + ".png")
    plt.clf()

# print("선생님 나빠요 학생 낚이라고 막 함정 파 놓으시고 기다리시고")
# print("진짜 나쁘셨다...")

print(df_num.corr())
sns.heatmap(df_num.corr(), annot=True)

pd.pivot_table(data, index='Survived', values = num_var)
# sns.barplot(x=df_cat[cat_var[0]].value_counts().index, y=df_cat[cat_var[0]].value_counts()).set_title(cat_var[0])


# data['numeric_ticket'] = data.Ticket.apply(lambda x: 1 if x.isnumeric() else 0)
# data['name_title'] = data.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())

train_X = df_num
train_y = data['Survived']

model = LinearRegression().fit(train_X, train_y)
model.predict(train_X)
predicted_values = model.predict(train_X)
predicted_values = pd.DataFrame(predicted_values) >= 0.475
predicted_values = predicted_values.astype(int)
print(accuracy_score(train_y, predicted_values))
