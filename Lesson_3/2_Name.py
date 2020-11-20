# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def get_name(name, surname, date, city, mail, phone):
    return print(f"имя: {name}, фамилия: {surname}, д.р.: {date}, город: {city}, почта: {mail}, тел.: {phone}")


inp_1 = input("Имя: ")
inp_2 = input("фамилия: ")
inp_3 = input("д.р.: ")
inp_4 = input("город: ")
inp_5 = input("почта: ")
inp_6 = input("тел.: ")

get_name(name=inp_1, surname=inp_2, date=inp_3, city=inp_4, mail=inp_5, phone=inp_6)
