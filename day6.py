class Employee:
    def __init__(self, name, position, salary) -> None:
        self.name = name
        self.position = position
        self.salary = salary

    def anusal(self):
        print(f"Annual Salary of {self.name} working as {self.position} is getting a total package of {self.salary * 12}")


e1 = Employee("Rahul", "Tech Lead", 35000)
e1.anusal()


class Triangle:
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2
    
t1 = Triangle(10,30)
print("For base ", t1.base, " and height ", t1.height, " Area is ",t1.area())