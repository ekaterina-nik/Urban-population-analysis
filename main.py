import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
test = pd.read_csv('C:/Users/Екатерина/Downloads/forFBpost.csv', sep = ';')
print(test.shape)
print(test.dtypes)
print(test.duplicated().sum())
print(test.head(5))
a = test.rename(columns = {'Город': 'city', 'Модель': 'model', 'Нижняя граница': 'lower_bound', 'Верхняя граница': 'upper_bound'})

a = a[(a.fact != 0) & (a.model != 0) & (a.model.notnull())]
print(a.head(5))
print(a.shape)

#c = a[['fact', 'model', 'lower_bound', 'upper_bound']]
#for column in c:
    #sns.displot(a, x = column, kde=True)
#b.plot(x = 'year', y = ['fact', 'model', 'lower_bound', 'upper_bound'])
e = a.groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False)
print(e)
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


#('A <= 80 & AUS > 100 & IND < 250')


#количество городов в каждом сегменте
l = a.query("segment == 'low'").city.nunique()
m = a.query("segment == 'middle'").city.nunique()
ll = a.query("segment == 'large'").city.nunique()
exll = a.query("segment == 'extra_large'").city.nunique()
print(l, m, ll, exll)

#среднее фактическое количество населения в каждом сегменте:
l1 = a.query("segment == 'low'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
m1 = a.query("segment == 'middle'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
ll1 = a.query("segment == 'large'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
exll1 = a.query("segment == 'extra_large'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending = False).mean()
print(l1, m1, ll1, exll1)

#df[df['my_column'] == df['my_column']. max ()]

#print(a[a['fact'] == a['fact'].mean()])

n = a.query("segment == 'low'")
n['difference'] = abs(n['fact'] - 37848)
print(n[n['difference'] == n['difference'].min()])
o = a.query("segment == 'middle'")
o['difference'] = abs(o['fact'] - 227000)
print(o[o['difference'] == o['difference'].min()])
p = a.query("segment == 'large'")
p['difference'] = abs(p['fact'] - 615454)
print(p[p['difference'] == p['difference'].min()])


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

#cities = a.city
#years = a.years
#plt.bar(cities, years)
#plt.title("A")
#plt.xlabel("город")
#plt.ylabel("год")
#plt.show

#plt.figure(figsize=(10, 10))
#l1 = a.query("segment == 'low'").groupby('city').aggregate({'fact': 'mean'}).sort_values('fact', ascending=False).head(10)
#l1.plot(kind = 'bar').set_title('low сегмент')
#plt.show

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








a.query("city == 'Сокол' & year <= 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Сокол')

a.query("city == 'Химки' & year <= 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Химки')

a.query("city == 'Ярославль' & year <= 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Ярославль')

a.query("city == 'Москва' & year < 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Москва')

a.query("city == 'Краснодар' & year < 2037").plot(x='year', y=['fact', 'model'], kind='bar').set_title('Краснодар')
plt.show


print(a.query("city == 'Краснодар'").aggregate({'fact': 'mean'}))





