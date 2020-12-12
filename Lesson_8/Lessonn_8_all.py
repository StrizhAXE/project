# 1. -------------------------------------------------------------------------------------------------------------------
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
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

# 2. -------------------------------------------------------------------------------------------------------------------
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
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

# 3. -------------------------------------------------------------------------------------------------------------------
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class WrongType(Exception):
    """ проверяет введеный элемент на число """

    def __init__(self, user_el):
        self.el = user_el

    @property
    def check_isdigit(self):
        try:
            if self.el.isdigit():
                res = int(self.el)
                return res
            else:
                raise WrongType("Не число")
        except WrongType as Err:
            print(Err)


res_list = []
while True:
    u_inp = input("Введите число для добавления в список, для выхода X: ")
    if u_inp in ["x", "X", "х", "Х"]:
        print(f"Итоговый список: {res_list}")
        print(f"Выход -->")
        break
    else:
        WT_res = WrongType(u_inp).check_isdigit
        if WT_res is not None:
            res_list.append(WT_res)
            print(f"Итоговый список: {res_list}")

# 4. -------------------------------------------------------------------------------------------------------------------
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Store:
    def __init__(self):
        self.capacity = 100


class OgrTech:
    def __init__(self, num_branch=50):
        self.num_branch = num_branch


class Printer(OgrTech):
    def __init__(self, color):
        super().__init__()
        self.color = color


class Scanner(OgrTech):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Xerox(OgrTech):
    def __init__(self, label):
        super().__init__()
        self.label = label

# 5. -------------------------------------------------------------------------------------------------------------------
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

import json


class Store:
    def __init__(self):
        self.database_file = "database.txt"

    @classmethod
    def addtostore(cls, product):
        database_store = {}
        cls.prod = product
        if cls.prod[0].lower() == "printer":
            database_store = Printer(cls.prod).get_spec()
        elif cls.prod[0].lower() == "scanner":
            database_store = Scanner(cls.prod).get_spec()
        elif cls.prod[0].lower() == "xerox":
            database_store = Xerox(cls.prod).get_spec()
        if database_store != {}:
            cls.add_to_file_base(cls(), database_store)
        else:
            print(f"Не подходящие данные для записи")
        return True

    def add_to_file_base(self, data):
        with open(self.database_file, "a", encoding="utf-8") as file_:
            j_str = json.dumps(data)
            data.clear()
            file_.write(f"{j_str}\n")
        print(f"Данные записаны в файл")


class OgrTech:
    def __init__(self):
        self.sc_branch = "Branch_scan"
        self.pr_branch = "Branch_print"
        self.xe_branch = "Branch_xerox"


class Printer(OgrTech):
    def __init__(self, prod):
        super().__init__()
        self.color = "Grey"
        self.prod = prod

    def get_spec(self):
        res = {"branch": self.pr_branch, "type": self.prod[0], "name": self.prod[1], "number": self.prod[2],
               "color": self.color}
        return res


class Scanner(OgrTech):
    def __init__(self, prod):
        super().__init__()
        self.description = "Сканер на склад"
        self.prod = prod

    def get_spec(self):
        res = {"branch": self.sc_branch, "type": self.prod[0], "name": self.prod[1], "number": self.prod[2],
               "description": self.description}
        return res


class Xerox(OgrTech):
    def __init__(self, prod):
        super().__init__()
        self.label = "Копировальный аппарат"
        self.prod = prod

    def get_spec(self):
        res = {"branch": self.xe_branch, "type": self.prod[0], "name": self.prod[1], "number": self.prod[2],
               "label": self.label}
        return res


product_item = ["HW", "HP", 5]
Store.addtostore(product_item)
product_item = ["printer", "HP", 4]
Store.addtostore(product_item)
product_item = ["printer", "HP", 3]
Store.addtostore(product_item)
product_item = ["scanner", "canon", 3]
Store.addtostore(product_item)
product_item = ["xerox", "xerox", 2]
Store.addtostore(product_item)

# 6. -------------------------------------------------------------------------------------------------------------------
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

import json


class Store:
    def __init__(self):
        self.database_file = "database.txt"

    @staticmethod
    def input_item():
        item = []
        u_inp = input(f"Выберете тип оборудования:\n1 - принтер\n2 - сканер\n3 - копир\n4 - свой вариант\n")
        if u_inp == "1":
            item.append("printer")
        elif u_inp == "2":
            item.append("scanner")
        elif u_inp == "3":
            item.append("xerox")
        elif u_inp == "4":
            item.append(input(f"Наименование:"))
        item.append(input(f"Марка: "))
        while True:
            u_inp = input(f"Количество: ")
            if u_inp.isdigit():
                item.append(int(u_inp))
                break
            else:
                print(f"Не число, введите заново: ")
        return item

    @classmethod
    def addtostore(cls, product):
        database_store = {}
        cls.prod = product
        if cls.prod[0].lower() == "printer":
            database_store = Printer(cls.prod).get_spec()
        elif cls.prod[0].lower() == "scanner":
            database_store = Scanner(cls.prod).get_spec()
        elif cls.prod[0].lower() == "xerox":
            database_store = Xerox(cls.prod).get_spec()
        if database_store != {}:
            cls.add_to_file_base(cls(), database_store)
        else:
            print(f"Не подходящие данные для записи")
        return True

    def add_to_file_base(self, data):
        with open(self.database_file, "a", encoding="utf-8") as file_:
            j_str = json.dumps(data)
            data.clear()
            file_.write(f"{j_str}\n")
        print(f"Данные записаны в файл")


class OgrTech:
    def __init__(self):
        self.sc_branch = "Branch_scan"
        self.pr_branch = "Branch_print"
        self.xe_branch = "Branch_xerox"


class Printer(OgrTech):
    def __init__(self, prod):
        super().__init__()
        self.color = "Grey"
        self.prod = prod

    def get_spec(self):
        res = {"branch": self.pr_branch, "type": self.prod[0], "name": self.prod[1], "number": self.prod[2],
               "color": self.color}
        return res


class Scanner(OgrTech):
    def __init__(self, prod):
        super().__init__()
        self.description = "Сканер на склад"
        self.prod = prod

    def get_spec(self):
        res = {"branch": self.sc_branch, "type": self.prod[0], "name": self.prod[1], "number": self.prod[2],
               "description": self.description}
        return res


class Xerox(OgrTech):
    def __init__(self, prod):
        super().__init__()
        self.label = "Копировальный аппарат"
        self.prod = prod

    def get_spec(self):
        res = {"branch": self.xe_branch, "type": self.prod[0], "name": self.prod[1], "number": self.prod[2],
               "label": self.label}
        return res


Store.addtostore(Store.input_item())

# product_item = ["HW", "HP", 5]
# Store.addtostore(product_item)
# product_item = ["printer", "HP", 4]
# Store.addtostore(product_item)
# product_item = ["printer", "HP", 3]
# Store.addtostore(product_item)
# product_item = ["scanner", "canon", 3]
# Store.addtostore(product_item)
# product_item = ["xerox", "xerox", 2]
# Store.addtostore(product_item)

# 7. -------------------------------------------------------------------------------------------------------------------
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        c_sum = [0, 0]
        for i in range(2):
            c_sum[i] = (self.complex_num[i] + other.complex_num[i])
        return c_sum

    def __mul__(self, other):
        x = self.complex_num
        y = other.complex_num
        return [x[0] * y[0] - x[1] * y[1], x[0] * y[0] + x[1] * y[1]]


comp_num_1 = (1, 5)
comp_num_2 = (6, 5)
complex_1 = Complex(comp_num_1)
complex_2 = Complex(comp_num_2)
print(f"Сумма {comp_num_1} и {comp_num_2} = {complex_1 + complex_2}")
print(f"Произведение {comp_num_1} и {comp_num_2} = {complex_1 * complex_2}")
