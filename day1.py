
#1
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

data = Person('Rahul', 34)
print(data.name)
print(data.age)


#2
class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

mycar = Car('Tata', 'Tiago', 2021)

print (mycar.make, mycar.model, mycar.year)



#3
class circle_area:
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        pi = 22/7
        return pi * self.radius ** 2
    
c = circle_area(5)
print(c.area())