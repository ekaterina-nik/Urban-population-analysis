import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
test = pd.read_csv(''https://.../forFBpost.csv', sep = ';')
print(test.shape) # размерность датафрейма
print(test.dtypes) # типы данных
print(test.duplicated().sum()) # проверим, есть ли дублирующиеся строки (нет)
print(test.head(5)) # выведем первые 5 строк датафрейма
a = test.rename(columns = {'Город': 'city', 'Модель': 'model', 'Нижняя граница': 'lower_bound', 'Верхняя граница': 'upper_bound'}) # переименуем колонки более корректно

a = a[(a.fact != 0) & (a.model != 0) & (a.model.notnull())] # подготовка данных - оставляем только данные с ненулевыми значениями в колонках fact и model 
# и с заполненными в колонке model
                   
print(a.head(5))
print(a.shape)

e = a.groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False) # вычислим величину средней фактической численности населения для каждого города
print(e)

# сегментируем весь датафрейм на 4 части - в зависимости от численности населения (127138 - средняя численность по всему датафрейму, 
# остальные критерии взяты из определения мелких, средних и крупных городов)                   
def segment(row):
    if row < 127138:
        return 'low'
    if row > 127138 and row < 500000:
        return 'middle'
    if row > 500000 and row < 1000000:
        return 'large'
    if row >= 1000000:
        return 'extra_large'
a['segment'] = a.fact.apply(segment)
a['inaccuracy'] = (a.upper_bound - a.lower_bound)/2
print(a.head(10))


#количество городов в каждом сегменте
l = a.query("segment == 'low'").city.nunique()
m = a.query("segment == 'middle'").city.nunique()
ll = a.query("segment == 'large'").city.nunique()
exll = a.query("segment == 'extra_large'").city.nunique()
print(l, m, ll, exll)

#средняя фактическая численность населения по городам в каждом сегменте:
l1 = a.query("segment == 'low'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
m1 = a.query("segment == 'middle'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
ll1 = a.query("segment == 'large'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
exll1 = a.query("segment == 'extra_large'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
print(l1, m1, ll1, exll1)

#посчитаем для каждого из сегментов low, middle, large для каждого города величину отклонения среднего фактического количества жителей от среднего по сегменту, 
#найдем в каждой группе город с минимальным отклонением от среднего по сегменту
n = a.query("segment == 'low'")
n['difference'] = abs(n['fact'] - 37848)
print(n[n['difference'] == n['difference'].min()])
o = a.query("segment == 'middle'")
o['difference'] = abs(o['fact'] - 227000)
print(o[o['difference'] == o['difference'].min()])
p = a.query("segment == 'large'")
p['difference'] = abs(p['fact'] - 615454)
print(p[p['difference'] == p['difference'].min()])

# это будут города Сокол, Химки и Ярославль
# для этих городов построим распределение фактической и смоделированной численности населения в зависимости от года (диапазон возьмем до 2030 года):
plt.figure(figsize=(25, 15))

plt.subplot(2, 3, 1)
plt.xlabel("год", fontsize=8)
plt.ylabel("зависимости фактической и смоделированной численности населения", fontsize=8)
plt.grid()
z = a.query("city == 'Сокол' & year <= 2030")
plt.plot(z.year, z.fact, label='факт')
plt.plot(z.year, z.model, label='модель')
plt.title("Сокол")
plt.legend()

plt.subplot(2, 3, 2)
plt.xlabel("год", fontsize=8)
plt.ylabel("зависимости фактической и смоделированной численности населения", fontsize=8)
plt.grid()
y = a.query("city == 'Химки' & year <= 2030")
plt.plot(y.year, y.fact, label='факт')
plt.plot(y.year, y.model, label='модель')
plt.title("Химки")

plt.subplot(2, 3, 3)
plt.xlabel("год", fontsize=8)
plt.ylabel("зависимости фактической и смоделированной численности населения", fontsize=8)
plt.grid()
x = a.query("city == 'Ярославль' & year <= 2030")
plt.plot(x.year, x.fact, label='факт')
plt.plot(x.year, x.model, label='модель')
plt.title("Ярославль")

plt.subplot(2, 3, 4)
plt.xlabel("год", fontsize=8)
plt.ylabel("зависимости фактической и смоделированной численности населения", fontsize=8)
plt.grid()
d = a.query("city == 'Москва' & year <= 2030")
plt.plot(d.year, d.fact, label='факт')
plt.plot(d.year, d.model, label='модель')
plt.title("Москва")

plt.subplot(2, 3, 5)
plt.xlabel("год", fontsize=8)
plt.ylabel("зависимости фактической и смоделированной численности населения", fontsize=8)
plt.grid()
i = a.query("city == 'Краснодар' & year <= 2030")
plt.plot(i.year, i.fact, label='факт')
plt.plot(i.year, i.model, label='модель')
plt.title("Краснодар")
plt.show

# выборочно построим графики среднего значения численности населения для 5-ти городов из каждого сегмента
plt.figure(figsize=(25, 15))

plt.subplot(2, 2, 1)
plt.xlabel("город", fontsize=8)
plt.ylabel("средняя фактическая численность населения", fontsize=8)
plt.grid()
l1 = a.query("segment == 'low'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending=False).head(5)
plt.plot(l1)
plt.title('low сегмент')

plt.subplot(2, 2, 2)
plt.xlabel("город", fontsize=8)
plt.ylabel("средняя фактическая численность населения", fontsize=8)
plt.grid()
m1 = a.query("segment == 'middle'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending=False).head(5)
plt.plot(m1)
plt.title('middle сегмент')

plt.subplot(2, 2, 3)
plt.xlabel("город", fontsize=8)
plt.ylabel("средняя фактическая численность населения", fontsize=8)
plt.grid()
ll1 = a.query("segment == 'large'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending=False).head(5)
plt.plot(ll1)
plt.title('large сегмент')

plt.subplot(2, 2, 4)
plt.xlabel("город", fontsize=8)
plt.ylabel("средняя фактическая численность населения", fontsize=8)
plt.grid()
exll1 = a.query("segment == 'extra_large'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending=False)
plt.plot(exll1)
plt.title('extra large сегмент')

# построим также барплоты для трех выбранных городов из сегментов low, middle, large и для двух городов из сегмента extra large (Москва и Краснодар)
a.query("city == 'Сокол' & year <= 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Сокол')

a.query("city == 'Химки' & year <= 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Химки')

a.query("city == 'Ярославль' & year <= 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Ярославль')

a.query("city == 'Москва' & year < 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Москва')

a.query("city == 'Краснодар' & year < 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Краснодар')
plt.show

# можно заметить, что Краснодар одновременно попал в 2 выборки, large и extra large, что связано с тем, что в один период времени фактическое население в городе
# находилось в диапазоне 500000 - 1000000, а потом увеличилось и стало более 1000000, но тем не менее среднее фактическое значение меньше миллиона и составляет 906706.
print(a.query("city == 'Краснодар'").aggregate({'fact': 'mean'}))





