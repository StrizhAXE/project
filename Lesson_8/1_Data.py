# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». # Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    date = ""

    def __init__(self, date_str):
        Data.date = date_str.split("-")

    @classmethod
    def get_date(cls):
        try:
            dd = int(cls.date[0])
            mm = int(cls.date[1])
            yyyy = int(cls.date[2])
            return dd, mm, yyyy
        except ValueError:
            return "Введены не числа"
        except IndexError:
            return "Не верный формат строки"

    @staticmethod
    def validate():
        if Data.get_date()[0] in range(1, 32):
            if Data.get_date()[1] in range(1, 13):
                if str(Data.get_date()[2]).isdigit():
                    print(f"Дата верная")
                else:
                    print(f"Дата не верная")
            else:
                print(f"Дата не верная")
        else:
            print(f"Дата не верная")


Data("17-021985")
Data.validate()
print(Data.get_date())
Data("17-02aa-1985")
print(Data.get_date())
Data("17-02-1985")
print(Data.get_date())
Data.validate()
