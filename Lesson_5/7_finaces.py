# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json


def read_file(file_name):
    firm_dict = {}
    with open(file_name, "r", encoding="utf-8") as file_:
        while True:
            line = file_.readline()
            if line == "":
                break
            else:
                firm = line.split()[0]
                income = int(line.split()[2])
                consumption = int(line.split()[3])
                firm_temp = {firm: income - consumption}
                firm_dict.update(firm_temp)
    return firm_dict


def get_average_profit(firms_):
    profit = 0
    n_profit = 0
    for key in firms:
        if firms_[key] >= 0:
            profit += firms_[key]
            n_profit += 1
    average_profit = round(profit / n_profit)
    return {"average_profit": average_profit}


def write_json_(data):
    with open("firms.json", "w", encoding="utf-8") as file_:
        json.dump(data, file_)
        print(f"JSON: {json.dumps(data)}")


firms = (read_file("firms.txt"))
res_list = [firms, get_average_profit(firms)]
print(res_list)
write_json_(res_list)
