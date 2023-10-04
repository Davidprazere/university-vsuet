#Вывод нечётных чисел от A до B в порядке убывания:
A = int(input("Введите A: "))
B = int(input("Введите B: "))
if A % 2 == 0:
    A += 1
for i in range(B, A - 1, -2):
    print(i)