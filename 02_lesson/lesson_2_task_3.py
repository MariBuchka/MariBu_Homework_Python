import math

def square(arg):
    return math.ceil(math.pow(arg, 2))
# возможны и другие варианты:
#   return math.ceil(arg ** 2)
#   return math.ceil(arg * arg)

num_arg = float(input("Введите сторону квадрата a = "))

print(f"Площадь квадрата S = a^2 = {square(num_arg)}")