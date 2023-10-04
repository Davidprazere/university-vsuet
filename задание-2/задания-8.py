#Вывод лесенки из п ступенек:
p = int(input("Введите натуральное число p: "))
for i in range(1, p + 1):
    print("".join(str(j) for j in range(1, i + 1)))
