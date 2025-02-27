# 1 Создание переменной
my_heigh = 160
print(my_heigh)

# 2 Перезапись переменной
my_name = "Mari"
my_name = "Mari Bulycheva"
print(my_name)

# 3 Получение пользовательского ввода
pet_name = input("Как зовут Вашего питомца? ")
print("Ваш любимчик - " + pet_name)

# 4 Создание функции
def print_python():
    print("Учу Python!")

print_python()

# 5 Параметризация функций
def print_letter(let):
    print(let, end='')

print_letter('С')
print_letter('т')
print_letter('у')
print_letter('д')
print_letter('е')
print_letter('н')
print_letter('т')