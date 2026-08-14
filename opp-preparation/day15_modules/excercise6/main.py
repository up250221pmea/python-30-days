# Exercise 6 - Student Manager

from calculations import calculate_average as prom 
from students import create_student as stu 

student_name = "John"

grades = [90, 85, 95]


student = stu(student_name, grades)

average = prom(grades)


print(f"Student: {student['name']}")
print(f"Grades: {student['grades']}")
print(f"Average: {average}")