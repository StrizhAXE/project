# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = list(range(11))

month = input("Введите номер месяца от 1 до  12: ")

while not month.isdigit():
    month = input("Не верно, попробуйте еще раз: ")

if int(month) > 12 or int(month) == 0:
    month = input("Такого месяца не существует, попробуйте еще раз: ")
x = int(month)

if x in [1, 2, 12]:
    print("Зима")
elif x in [3, 4, 5]:
    print("Весна")
elif x in [6, 7, 8]:
    print("Лето")
elif x in [9, 10, 11]:
    print("Осень")

seasons = {1: "{Winter}", 2: "{Spring}", 3: "{Summer}", 4: "{Autumn}"}

if x in [1, 2, 12]:
    print(seasons.get(1))
elif x in [3, 4, 5]:
    print(seasons.get(2))
elif x in [6, 7, 8]:
    print(seasons.get(3))
elif x in [9, 10, 11]:
    print(seasons.get(4))
