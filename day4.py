class student:
    def __init__(self, name, age, marks) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def grade(self, total):
        final_grade = self.marks/total

        if final_grade > 0.9:
            return "A Grade"
        elif final_grade > 0.6:
            return "B Grade"
        else:
            return "C Grade"
        
s1 = student('Rahul', 33, 87)
grade_acq = s1.grade(100)

print(f"{s1.name} acquire an {grade_acq}")


import numpy as np

class circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return np.pi * (self.radius)** 2
    
    def circum(self):
        return 2 * np.pi * self.radius

c1 = circle(5)
area = c1.area()
circumference = c1.circum()

print(f"Area of the circle is {round(area,2)} and circumference is {round(circumference,2)}")