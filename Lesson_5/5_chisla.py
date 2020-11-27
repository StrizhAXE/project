# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


def cr_file(list_num):
    with open("5_numbers.txt", "w", encoding="utf-8") as file_num:
        for i in range(len(list_num)):
            file_num.write(str(list_num[i]) + " ")


def get_sum_from_file():
    with open("5_numbers.txt", "r", encoding="utf-8") as file_num:
        line = file_num.read().split()
        summa = 0
        for i in range(len(line)):
            summa += int(line[i])
    return summa


numbs = [randint(0, 100) for _ in range(10)]
print(f"Исходные рандомные числа: {numbs}")
cr_file(numbs)
print(f"Сумма чисел в файле: {get_sum_from_file()}")
