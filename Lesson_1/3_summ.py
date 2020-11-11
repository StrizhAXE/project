number = input("введите число: ")

while not number.isdigit():
    number = input("это не число, попробуйте еще раз: ")

str_num_sum_1 = number
str_num_sum_2 = number + number
str_num_sum_3 = number + number + number
str_num_sum = int(str_num_sum_1) + int(str_num_sum_2) + int(str_num_sum_3)
print(f"Сумма вида n + nn + nnn равна: {str_num_sum}")
