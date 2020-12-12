# 6. Реализуйте механизм валидации вводимых пользователем данных.
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
