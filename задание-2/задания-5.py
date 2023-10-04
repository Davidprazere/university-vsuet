#Вычисление суммы ряда:
p = int(input("Введите натуральное число p: "))
total = 0
for i in range(1, p + 1):
    total += 1 / (2 ** i)
print("Сумма ряда:", total)
