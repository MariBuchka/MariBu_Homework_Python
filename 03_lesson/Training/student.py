class Student:
    def __init__(self, first_name, last_name, age, course): # КОНСТРУКТОР описывает принимаемые параметры (сохраняет атрибуты объекта)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} лет, учится на курсе {self.course}"