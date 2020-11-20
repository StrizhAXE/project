# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def get_sum_numbers(list_numbers):
    sum_m = 0
    for x in range(len(list_numbers)):
        sum_m = sum_m + list_numbers[x]
    return sum_m


def input_num():
    while True:
        try:
            u_str = input("Введите числа через пробел,\nдля завершения ввода добавьте #,\nпример 10 10 10 #: ")
            numbers_str = u_str.split()
            for i in range(len(numbers_str)):
                if numbers_str[i] != "#":
                    numbers.append(float(numbers_str[i]))
                else:
                    global flag_end
                    flag_end = "#"
                    break
            break
        except ValueError:
            print("Неверный ввод")
    return numbers


numbers = []
flag_end = ""

while flag_end != "#":
    input_num()
    print(f"Сумма чисел: {get_sum_numbers(numbers)}")
    print("Продолжаем") if flag_end != "#" else print("Программа завершена")
