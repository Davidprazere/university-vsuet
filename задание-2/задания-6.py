#Вычисление факториала:
p = int(input("Введите натуральное число p: "))
factorial = 1
for i in range(1, p + 1):
    factorial *= i
print("Факториал числа", p, ":", factorial)
