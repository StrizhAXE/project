# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

with open("2nd.txt", "w", encoding="utf-8") as file_:
    while True:
        u_str = input("Введите строку: ") + "\n"
        if u_str != "\n":
            file_.writelines(u_str)
        else:
            break

with open("2nd.txt", "r", encoding="utf-8") as file_:
    n_str = 0
    for line in file_:
        print(f"{line}    Слов в строке: {len(line.split())}")
        n_str += 1
    print(f"Количество срок: {n_str}")
