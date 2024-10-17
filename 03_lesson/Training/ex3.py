from student import Student
from course_group import CourseGroup

student = Student("Иван", "Иванов", 28, "QA")
classmate1 = Student("Пётр", "Петров", 33, "QA")
classmate2 = Student("Марина", "Сидорова", 29, "QA")
classmate3 = Student("Злата", "Солнечная", 27, "QA")
classmate4 = Student("Alex", "Kremer", 28, "QA")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3, classmate4])

print(course_group)