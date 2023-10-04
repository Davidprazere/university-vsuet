
#Вывод чисел от D до V в порядке возрастания или убывания:
D = int(input("Введите D: "))
V = int(input("Введите V: "))
if D < V:
    for i in range(D, V + 1):
        print(i)
else:
    for i in range(D, V - 1, -1):
        print(i)
