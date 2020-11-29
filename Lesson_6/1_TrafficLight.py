# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:красный,желтый, зеленый
# Продолжительность первого состояния
# (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
# pip install colorama

from colorama import Fore
from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ["RED", "YELLOW", "GREEN"]

    def running(self, color_list):
        stop = 0
        if color_list == self.__color:
            for color in cycle(color_list):
                if color == "RED":
                    print(Fore.RED + "Красный")
                    sleep(7)
                elif color == "YELLOW":
                    print(Fore.YELLOW + "Желтый")
                    sleep(2)
                elif color == "GREEN":
                    print(Fore.GREEN + "Зеленый")
                    sleep(5)
                if stop == 5:
                    print(f"{Fore.RESET}STOP")
                    break
                stop += 1
                # print(stop)
        else:
            print(f"{Fore.RESET}Не верный порядок цветов")


TrafficLight().running(["RED", "YELLOW", "GREEN"])
TrafficLight().running(["YELLOW", "GREEN", "RED"])
