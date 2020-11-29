# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ""

    def draw(self):
        print(f"Запуск отрисовки для {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Ручка")


class Pencil(Stationery):
    def draw(self):
        print(f"Карандаш")


class Handle(Stationery):
    def draw(self):
        print(f"Управлять")


Stationery.title = "Рисунок_1"
Stationery().draw()
Pen().draw()
Pencil().draw()
Handle().draw()
