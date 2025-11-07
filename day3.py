class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

r = rectangle(100,50)
print(r.area())


class employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}\nDesg: {self.designation}\nSalary: {self.salary} Lakhs")

e = employee('Rahul', 'Tech Lead', 18)
e.display()