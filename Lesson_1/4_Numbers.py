# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("введите целое положительное число: ")

while not number.isdigit():
    number = input("Это не число, попробуйте еще раз: ")

list_num = list(number)

i = 0
max_num = int(list_num[i])

while i < len(list_num) - 1:
    n_list = int(list_num[i + 1])
    if max_num > int(n_list):
        i += 1
    else:
        max_num = int(n_list)
        i += 1

print(f"Максимальная цифра: {max_num}")
