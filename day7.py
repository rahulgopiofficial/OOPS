class student:
    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade

    def average_grade(self):
        return sum(self.grade)/len(self.grade)
    
s1 = student('Rahul', [45,44,32,48,39,49])
print(round(s1.average_grade(),2))