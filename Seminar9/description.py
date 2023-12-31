# Описание базы данных
# 3. Выведите сводную информацию по базе данных: какие переменные в ней есть, какого они типа +
# сколько заполненных наблюдений в каждой столбце.
# 4. Выведите сводную статистическую информацию по каждому количественному показателю в базе
# (описательные статистике).
# 5. Постройте гистограмму для переменной Возраст (Age), сделайте ее красного цвета, подпишите оси
# и добавьте заголовок графика.
# 6. Выведите описательные статистики для столбца Стоимость билета (Fare).

# 3
import pandas as pd
df = pd.read_csv('Titanic.csv')

df.info()

# 4
print(df.describe())

# 6
print(df['Fare'].describe())

# 5
import matplotlib.pyplot as plt

df['Age'].plot.hist(color = 'red')

plt.xlabel("Возраст")
plt.ylabel("Количество пассажиров")
plt.title("Гистограмма возраста")
plt.show()


