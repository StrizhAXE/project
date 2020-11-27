# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("1st.txt", "w", encoding="utf-8") as file_:
    while True:
        u_str = input("Введите данные: ") + "\n"
        if u_str != "\n":
            file_.writelines(u_str)
        else:
            break

with open("1st.txt", "r", encoding="utf-8") as file_:
    print(file_.read())
