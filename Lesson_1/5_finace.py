# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

plus = input("Введите выручку: ")
while not plus.isdigit():
    plus = input("Это не число, попробуйте еще раз: ")

minus = input("Введите издержки: ")
while not minus.isdigit():
    minus = input("Это не число, попробуйте еще раз: ")
plus = int(plus)
minus = int(minus)

if plus > minus:
    print("Хорошее финансовое положение")
    rent = round(plus / minus, 2)
    print(f"Рентабельность {rent}")
else:
    print("Убыточное предприятние, пора закрываться")
