# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("4_num_eng.txt", "r", encoding="utf-8") as file_eng:
    with open("4_num_rus.txt", "w", encoding="utf-8") as file_rus:
        for line in file_eng:
            line = line.replace("One", "Один")
            line = line.replace("Two", "Два")
            line = line.replace("Three", "Три")
            line = line.replace("Four", "Четыре")
            file_rus.write(line)
