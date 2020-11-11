hour = 0
minute = 0
second = 0

sek = input("введите время в секундах: ")

while not sek.isdigit():
    sek = input("это не число, попробуйте еще раз: ")

sek = int(sek)
hour = sek // 3600
minute = (sek - hour * 3600) // 60
second = int(sek - (hour * 3600 + minute * 60))

print(f"Время в формате hh:mm:ss - {hour}:{round(minute, 0)}:{round(second, 0)}")
