# Импорт библитотеки
import pandas as pd
import numpy as np

pupils = ['Маша', 'Саша', 'Таня', 'Света', 'Петя', 'Сережа', 'Дима', 'Катя', 'Ваня', 'Лена']
lessons = ['Математика', 'История', 'Литература', 'География', 'Физика']

df = pd.DataFrame(index=pupils, columns=lessons)


# случайные оценки от 2 до 5
np.random.seed(0)
# Применение функции для заполнение датафрейма
# (Метод `apply` используется для применения функции к каждому элементу, строке или столбцу объекта DataFrame.
# Он позволяет выполнять различные операции над данными поэлементно или по строкам/столбцам.
df = df.apply(lambda x: np.random.randint(2, 6, size=len(df)))

print("Содержимое df:")
print(df)

print("Первые 5 строк:")
print(df.head())

print("Средние оценки по предметам:")
print(df[lessons].mean())

print("Медианные оценки по предметам:")
print(df[lessons].median())

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR = Q3_math - Q1_math
print(f"Q1 = {Q1_math}, Q3 = {Q3_math}, IQR = {IQR}")

print("Стандартные отклонения по предметам:")
print(df[lessons].std())
