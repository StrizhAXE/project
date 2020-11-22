# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint
source_list = [randint(0, 100) for i in range(20)]  # генерим исходный лист чисел
for i in range(len(source_list)):  # """Раширяем  рандомно повторениями 1/4 все элементов"""
    if randint(0, 3) == 3:
        source_list.insert(i, source_list[i])

res_list = []
for i in range(len(source_list)):  # Удаляем повторы
    res_list.append(source_list[i]) if source_list.count(source_list[i]) == 1 else res_list

print(f"Исходный список: {source_list}")
print(f"Список без элементов с повторами: {res_list}")
