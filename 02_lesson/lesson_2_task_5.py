def month_to_season(m):
    if (1 <= m <= 2) or (m == 12):
        return "Зима"
    elif 3 <= m <= 5:
        return "Весна"
    elif 6 <= m <= 8:
        return "Лето"
    elif 9 <= m <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"

try:
    m = int(input("Введите номер месяца (от 1 до 12 включительно): "))
    print(month_to_season(m))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")