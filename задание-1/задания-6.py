seconds = int(input("Введите количество секунд: "))  # Пользователь вводит количество секунд
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f"{days}:{hours}:{minutes}:{seconds}")