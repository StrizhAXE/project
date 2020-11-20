# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def get_degree_1(a, b):
    return 1 / (a ** abs(b))


def get_degree_2(a, b):
    a1 = a
    for i in range(abs(b) - 1):
        a1 = a1 * a
    return 1 / a1


while True:
    try:
        u_inp_a = input("Введите 2 числа, действительное положительное и целое отрицательное:\n")
        u_inp_b = input()
        stop = []
        inp_a = float(u_inp_a) if float(u_inp_a) > 0 else int("u_inp_a")
        inp_b = int(u_inp_b) if int(u_inp_b) < 0 else int("u_inp_b")
    except ValueError:
        print("Не верный ввод")
    else:
        break

print(type(inp_a), inp_a, type(inp_b), inp_b)
print(get_degree_1(inp_a, inp_b))
print(get_degree_2(inp_a, inp_b))
