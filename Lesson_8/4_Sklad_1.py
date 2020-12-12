# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
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
