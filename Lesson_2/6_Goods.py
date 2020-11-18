# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, Цена, Количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
price_list = []
price_list_temp = []
end_key = "start"
n = 0

sel = input("Использовать шаблон (0) или ввести данные (1): ")
if sel == "0":
    price_list = [(1, {'Название': 'Болт', 'Цена': '10', 'Количество': '10'}),
                  (2, {'Название': 'Гайка', 'Цена': '5', 'Количество': '20'}),
                  (3, {'Название': 'Хрень 1', 'Цена': '15', 'Количество': '7'}),
                  (4, {'Название': 'Хрень 2', 'Цена': '15', 'Количество': '19'})]
else:
    while end_key != "end":
        n += 1
        name = input("Название товара: ")
        price = input("Цена товара: ")
        numbers = input("Количесво товара: ")
        good_set = {'Название': name, 'Цена': price, 'Количество': numbers}
        price_list_temp.clear()
        price_list_temp.append(n)
        price_list_temp.append(good_set)
        price_list.append(tuple(price_list_temp))
        end_key = input("Для окончания ввода напишите end или продолжите ввод данных: ")
        print(price_list)

print("Заданные товары:")
for i in range(len(price_list)):
    print(f"{price_list[i]}")
print(f"\n")

sort_type = input('''Введите тип сортировки товаров:
1 - Название
2 - Цена
3 - Количество
''')

while sort_type not in ("1", "2", "3"):
    sort_type = input("Не верно, попробуйте еще раз: ")
sort_type = int(sort_type) - 1

goods_dict = {}
keys = price_list[0][1].keys()
x = list(keys)[sort_type]
val = []

for i in range(len(price_list)):
    dict_0 = price_list[i][1]
    val.append(dict_0.get(x))
    if i == (len(price_list) - 1):
        dict_0 = {x: val}
        goods_dict.update(dict_0)
print(f'Выборка по "{x}"\n{goods_dict}')

goods_dict = {}
dict_0 = {}
keys = price_list[0][1].keys()
# print(keys)

for x in keys:
    val = []
    for i in range(len(price_list)):
        dict_0 = price_list[i][1]
        val.append(dict_0.get(x))
        if i == (len(price_list) - 1):
            dict_0 = {x: val}
            goods_dict.update(dict_0)

print("\nВсе товары по категориям:")
for x in keys:
    print(f"{x}:{goods_dict.get(x)}")
