# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("3rd.txt", "w", encoding="utf-8") as file_:
    file_.writelines("Васильев 20000\nПетрова 30000\nИванов 150000\nПлюшкин 10000 ")

cost_dict = {}
with open("3rd.txt", "r", encoding="utf-8") as file_:
    for line in file_:
        line_dict = {line.split()[0]: line.split()[1]}
        cost_dict.update(line_dict)

for i in list(cost_dict.keys()):
    print(i)

cost = 0
n = 0
for i in list(cost_dict.values()):
    cost = cost + int(i)
    n += 1
print(f"Средняя ЗП: {round(cost / n)}")
