import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# game_name은 게임의 이름을 나타냅니다.
# game_price는 컴퓨터 게임의 가격을 나타내고 num_people은 게임을 좋아한 사람들의 수를 나타냅니다.
game_name = ['Phone of duty','PIFA soccer','Lario cart','Hokemon','Loom','League of failures','Fritnite','Fatty Trotter']
game_price = [10,20,50,150,80,200,1000,-100]
num_people = [1,2,5,15,8,10,1,0.5]

plt.scatter(num_people[0:5],game_price[0:5])
plt.scatter(num_people[5],game_price[5],c='g')
plt.scatter(num_people[6:8],game_price[6:8],c='r')

plt.xlabel('Number of People')
plt.ylabel('Price of game (USD)')

plt.show();

game_name = ['Phone of duty','PIFA soccer','Lario cart','Hokemon','Loom','League of failures','Fritnite','Fatty Trotter']
game_price = [10,20,50,150,80,200]
num_people = [1,2,5,15,8,10,1]

plt.scatter(num_people[0:5],game_price[0:5])
plt.scatter(num_people[5],game_price[5],c='r')
plt.scatter(num_people[5:6],game_price[5:6],c='g')

plt.xlabel('Number of People')
plt.ylabel('Price of game (USD)')

plt.show();

dir = 'C:/Users/15/Desktop/DataSet/'

df = pd.read_csv(dir+'[Dataset] Module17 (Students_Score1).csv')
print(df.head())
print(df.info())
print(df.describe())

df1 = df[df['Mathematics score']>=0]
df2 = df1[df1['Mathematics score']<=100]
print(df2.describe())

df1 = df2[df2['English score']>=0]
df2 = df1[df1['English score']<=100]
print(df2.describe())

df1 = df2[df2['Science score']>=0]
df2 = df1[df1['Science score']<=100]
print(df2.describe())
# print(df2['Mathematics score'].describe())

House_prices = [42300,50206,105000,22350]
Num_rooms = [4,5,10,2]

plt.scatter(Num_rooms,House_prices)
plt.xlabel('Number of rooms')
plt.ylabel('House prices in USD')
plt.show()

House_prices = [42300,50206,105000,22350,10050,60000,120000]
Num_rooms = [4,5,10,2,1,6,12]
plt.scatter(Num_rooms,House_prices)
plt.xlabel('Number of rooms')
plt.ylabel('House prices in USD')
plt.show()

df = pd.read_csv(dir+'[Dataset] Module 17 (Students_Score2).csv')#Nan 혹은 모두 0으로 표시된 데이터 없애기
print(df.head())
print(df.info())
print(df.describe())

df2 = df.dropna(axis=0)
print(df2.info())

df3 = df.copy()
print('Before filling------------------')
print(df3['Mathematics score'].describe())
df3['Mathematics score'] = df3['Mathematics score'].fillna(df['Mathematics score'].mean())
print('After fillna--------------------')
print(df3['Mathematics score'].describe())