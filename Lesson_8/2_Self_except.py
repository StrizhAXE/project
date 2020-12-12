# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class SelfExcept(Exception):
    def __init__(self, user_string):
        try:
            self.divider = float(user_string)
            if self.divider == 0:
                raise SelfExcept("Деление на ноль запрещено")
            else:
                print(f"divider = {self.divider}\nВсе нормас!")
        except ValueError:
            self.divider = None
            print(f"Не верный ввод")
        except SelfExcept as self_error:
            print(self_error)


while True:
    u_int = input("Введите делитель или х для выхода: ")
    if u_int != "x":
        SelfExcept(u_int)
    else:
        print(f"Выход --> ")
        break
