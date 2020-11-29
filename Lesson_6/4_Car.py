# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed=0, color="", name="Auto", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} Go-Go with speed {self.speed}")

    def stop(self):
        print(f"{self.name} {self.color} stop")

    def turn(self, direction):
        print(f"{self.name} turn {direction}")

    def show_speed(self):
        print(f"Car speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"TownCar speed is {self.speed}, exceeding the speed limit by {self.speed - 60} km !!!")
        else:
            print(f"TownCar speed is {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"WorkCar speed is {self.speed}, exceeding the speed limit by {self.speed - 40} km !!!")
        else:
            print(f"WorkCar speed is {self.speed}")


class SportCar(Car):
    def show_speed(self):
        if self.speed < 150:
            print(f"Car speed is {self.speed}, This is not SportCar")
        else:
            print(f"WorkCar speed is {self.speed}")


class PoliceCar(Car):
    def get_type(self):
        if self.is_police:
            print(f"Это машина полиции")
        else:
            print("Это не полиция")


Car(40).go()
Car(60, "Red", "Subaru").stop()
Car(60, "Red", "Subaru").turn("right")
Car(60, "Red", "Subaru").show_speed()
TownCar(40, "Red", "Subaru").show_speed()
TownCar(80, "Red", "Subaru").show_speed()
SportCar(100).show_speed()
SportCar(200).show_speed()
WorkCar(40, "Blue", "Subaru").show_speed()
WorkCar(80, "Blue", "Subaru").show_speed()
WorkCar(80, "Blue", "Subaru").go()
WorkCar(80, "Blue", "Subaru").turn("left")
PoliceCar(180, "Green", "Reno", True).stop()
PoliceCar(180, "Green", "Reno").get_type()
PoliceCar(180, "Green", "Reno", True).get_type()
