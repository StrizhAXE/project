# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
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
