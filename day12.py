import numpy as np

class circle:

    pi = round(np.pi,5)

    print(pi)

    def __init__(self, radius) -> None:
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def get_area(self):
        return round(circle.pi * np.square(self.radius), 2)

    def get_circum(self):
        return round(2 * circle.pi * self.radius, 2)
    
    @classmethod

    def compare_circle(cls, circle1, circle2):
        area1 = circle1.get_area()
        area2 = circle2.get_area()

        if area1 > area2:
            return 1
        elif area2 > area1:
            return -1
        else:
            return 0
    

c1 = circle(100)
print(f"The radius is {c1.get_radius()}, area is {c1.get_area()} and circumference is {c1.get_circum()}")
c2 = circle(50)
result = circle.compare_circle(c1, c2)
print(result)