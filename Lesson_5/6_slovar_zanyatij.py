# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных
# , практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def parser(name_file):
    with open(name_file, "r", encoding="utf-8") as file_:
        main_dict = {}
        while True:
            line = file_.readline()
            if line == "":
                break
            else:
                key = line.split(":")[0]
                hours_str = ""
                for i in range(len(line.split(":")[1])):
                    if line.split(":")[1][i].isdigit():
                        hours_str += line.split(":")[1][i]
                    else:
                        hours_str += " "
                hours_str = hours_str.split()
                hours = 0
                for i in range(len(hours_str)):
                    hours += int(hours_str[i])
                temp_dict = {key: hours}
                main_dict.update(temp_dict)
    return main_dict


print(parser("Предметы.txt"))
