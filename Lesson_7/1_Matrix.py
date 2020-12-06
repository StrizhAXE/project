# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    """ Обработка данных списков и формирование матрицы """
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists
        # print(self.matrix)

    def __str__(self):
        self.val = (lists for lists in self.matrix)
        for var in self.val:
            print(f"{var}")
        return "\n"

    def __add__(self, other):
        sum_mt = []
        for i in range(len(self.matrix)):
            temp_mt = []
            for j in range(len(self.matrix[i])):
                i_j = self.matrix[i][j] + other.matrix[i][j]
                temp_mt.append(i_j)
            sum_mt.append(temp_mt)
        return sum_mt


data1 = [[1, 2, 3], [4, 5, 6, 7], [0, -1, -2]]
data2 = [[1, 1, 1], [2, 2, 2, 2], [3, 3, 3]]
# print(data, type(data))
mt1 = Matrix(data1)
mt2 = Matrix(data2)
print(f"Матрица 1{mt1}")
print(f"Матрица 2{mt2}")
sum_data = mt1 + mt2
print(f"Сумарная матрица{Matrix(sum_data)}")
