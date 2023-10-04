#Вычисление суммы ряда 1 + 2! + 3! + ... + p!:
p = int(input("Введите натуральное число p: "))
total = 0
factorial = 1
for i in range(1, p + 1):
    factorial *= i
    total += factorial
print("Сумма ряда:", total)
