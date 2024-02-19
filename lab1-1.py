import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. Відкрити та зчитати файл з даними.
df = pd.read_csv('Vehicle_Sales.csv')
print('1.')
print('Таблиця Vehicle_Sales.csv:')
print(df) 
input()

#2. Визначити та вивести кількість записів та кількість полів у кожному записі.
num_of_rows = len(df)
num_of_columns = len(df.columns)
print('2.')
print('Кількість записів:', num_of_rows)
print('Кількість полів:', num_of_columns)
input()

#3. Вивести К+7 перших та 5К-3 останніх записів
k = 3
first_rows = df.head(k+7)
print('3.')
print('Перші k+7 записів:')
print(first_rows)

last_rows = df.tail(5*k-3) 

print('Останні 5*k-3 записів:')
print(last_rows)
input()

#4. Визначити та вивести тип полів кожного запису.
print('4.')
print('Тип полів кожного запису:')
print(df.dtypes)
input()

#5. Привести поля, що відповідають обсягам продаж, до числового вигляду (показати, що це виконано).
print('5.')
print('Таблиця після переведення полів, що відповідають обсягом продаж, до числового вигляду:')
df['Total Sales New'] = df['Total Sales New'].str.replace('$', '')
df['Total Sales Used'] = df['Total Sales Used'].str.replace('$', '')
df['Total Sales New'] = df['Total Sales New'].astype(np.int64)
df['Total Sales Used'] = df['Total Sales Used'].astype(np.int64)
print(df) 
print('Тип полів кожного запису:')
print(df.dtypes)
input()

#6. Ввести нові поля: a. Сумарний обсяг продаж автомобілів (нових та б/в) у кожний період; b. Сумарний дохід від продажу автомобілів (нових та б/в) у кожний період; c. Різницю в обсязі продаж нових та б/в автомобілів у кожній період.
print('6.')
print('Таблиця після введення нових полів:')
cols1 = ['New', 'Used']
df['Total volume'] = df[cols1].sum(axis= 1)
cols2 = ['Total Sales New', 'Total Sales Used']
df['Total income'] = df[cols2].sum(axis= 1)
df['Difference in the volume'] = df['Used'] - df['New']
print(df) 
input()

#7. Змінити порядок розташування полів таким чином: Рік, Місяць, Сумарний дохід, Дохід від продажу нових автомобілів, Дохід від продажу б/в автомобілів, Сумарний обсяг продаж, Обсяг продаж нових автомобілів, 
# Обсяг продаж б/в автомобілів, Різниця між обсягами продаж нових та б/в автомобілів
print('7.')
print('Таблиця після змінення порядку розташування полів:')
cols3 = ['Year', 'Month', 'Total income', 'Total Sales New', 'Total Sales Used', 'Total volume', 'New', 'Used', 'Difference in the volume']
df = df[cols3]
print(df)
input()

#8. Визначити та вивести: a. Рік та місяць, у які нових автомобілів було продано менше за б/в; b. Рік та місяць, коли сумарний дохід був мінімальним; c. Рік та місяць, коли було продано найбільше б/в авто.
print('8.а')
print('Рік та місяць, у які нових автомобілів було продано менше за б/в:')
cols4 = ['Year', 'Month']
df1=df.loc[df['New']<df['Used']]
df1=df1[cols4]
print(df1)

print('8.б')
print('Рік та місяць, коли сумарний дохід був мінімальним:')
df2=df.loc[df['Total income'].idxmin()]
df2=df2[cols4]
print(df2)

print('8.в')
print('Рік та місяць, коли було продано найбільше б/в авто:')
df3=df.loc[df['Used'].idxmax()]
df3=df3[cols4]
print(df3)
input()

#9. Визначити та вивести: a. Сумарний обсяг продажу транспортних засобів за кожен рік; b. Середній дохід від продажу б/в транспортних засобів в місяці М, де М – це порядковий номер у списку підгрупи за абеткою.
print('9.а')
print('Сумарний обсяг продажу транспортних засобів за кожен рік')
df4=df.groupby('Year', as_index=False)['Total volume'].sum()
print(df4)

print('9.б')
print('Середній дохід від продажу б/в транспортних засобів в місяці М, де М – це порядковий номер у списку підгрупи за абеткою:')
df5=df.loc[df['Month']=='MAR']
df5=df5['Total income'].mean()
print(df5)
input()

#10. Побудувати стовпчикову діаграму обсягу продаж нових авто у році 20YY, де дві останні цифри року визначаються як 17 – порядковий номер у списку підгрупи за абеткою.
print('10.')
print('Стовпчикова діаграма обсягу продаж нових авто у році 20YY, де дві останні цифри року визначаються як 17 – порядковий номер у списку підгрупи за абеткою.')
df6=df.loc[df['Year']==2014]
df6[['Month', 'New']].plot.bar(x='Month') 
plt.show()
input()

#11. Побудувати кругову діаграму сумарного обсягу продаж за кожен рік.
print('11.')
print('Кругова діаграма сумарного обсягу продаж за кожен рік.')
print(df4)
df4.plot.pie(y='Total volume', labels = df4['Year'])
plt.legend(labels = df4['Year'],loc = (1,0))
plt.show()
input()

#12. Побудувати на одному графіку: Сумарний дохід від продажу нових авто; Сумарний дохід від продажу старих авто
print('12.')
print('На одному графіку: Сумарний дохід від продажу нових авто; Сумарний дохід від продажу старих авто')
df7=df.groupby('Year')['Total Sales New'].sum()
df8=df.groupby('Year')['Total Sales Used'].sum()
df7.plot(x='Year', y='Total Sales New', label='Сумарний дохід від продажу нових авто')
df8.plot(x='Year', y='Total Sales Used', label='Сумарний дохід від продажу старих авто')
plt.legend()
plt.show()

input()
