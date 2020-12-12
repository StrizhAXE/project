# 7. Реализовать проект «Операции с комплексными числами».
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
