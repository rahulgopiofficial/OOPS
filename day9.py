class student:
    def __init__(self, name, grade, subject) -> None:
        self.name = name
        self.grade = grade
        self.subject = subject

    def add_sub(self, subject):
        self.subject.append(subject)
    
    def show_sub(self):
        print(self.subject)


s1 = student('Rahul', 'A', ['Coding', 'History'])
s1.add_sub('Math')
s1.add_sub('Science')

s1.show_sub()