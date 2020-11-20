# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    return (a + b + c) - min(a, b, c)


u_inp_a = input("Введите 3 числа\n")
u_inp_b = input()
u_inp_c = input()
while not u_inp_a.isdigit() or not u_inp_b.isdigit() or not u_inp_c.isdigit():
    u_inp_a = input("Не верно, попробуйте еще раз: \n")
    u_inp_b = input()
    u_inp_c = input()

print(f"Сумма наибольших чисел: {my_func(int(u_inp_a), int(u_inp_b), int(u_inp_c))}")
