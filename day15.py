# In below approach i am using school name and creting based on instance here there is no need to change using class method
# Because i am changing for instance and it will not affect the class attribute as whole

class School:
    school_name = ""

    def __init__(self, school_name):
        School.school_name = school_name
        self.teacher = []
        self.student = []
        self.student_count = 0
        self.teacher_count = 0

    def add(self, type, name):
        if type == 'T':
            self.teacher.append(name)
            self.teacher_count += 1
        elif type == 'S':
            self.student.append(name)
            self.student_count += 1

    @classmethod
    def change_school_name(cls, new_name):
        School.school_name = new_name

c1 = School('DPS')
c1.add('T','Rajakumari')
c1.add('T','Sweety')

c1.add('S','Rajesh')
c1.add('S','Rahul')

c2 = School('NPS')
c2.add('T','Aishu')
c2.add('T','Shinoj')

c2.add('S','Mahesh')
c2.add('S','Midhun')


print(f"{c1.school_name} \t\t Teacher: {c1.teacher_count} \t\t Student: {c1.student_count}")
print(c1.student, c1.teacher)
print(f"{c2.school_name} \t\t Teacher: {c2.teacher_count} \t\t Student: {c2.student_count}")
print(c2.student, c2.teacher)


# Alternate method and as per question
# Here you created a variable school name and using classmethod you are changing the name
# changing the name using classmethod will affect all the instance because it is class attribute
# -------------------


# class School:
#     school_name = ""  # Class-level attribute

#     def __init__(self, school_name):
#         School.school_name = school_name
#         self.student_count = 0
#         self.teacher_count = 0
#         self.students = []
#         self.teachers = []

#     def add_student(self, student_name):
#         self.students.append(student_name)
#         self.student_count += 1

#     def add_teacher(self, teacher_name):
#         self.teachers.append(teacher_name)
#         self.teacher_count += 1

#     def summary(self):
#         print(f"School Name (class-level): {School.school_name}")
#         print(f"Instance: Students({self.student_count}) Teachers({self.teacher_count})")
#         print(f"Students List: {self.students}")
#         print(f"Teachers List: {self.teachers}")
#         print("-" * 40)

#     @classmethod
#     def change_school_name(cls, new_name):
#         cls.school_name = new_name


# # Create three School instances
# s1 = School('DPS')
# s1.add_student('Rajesh')
# s1.add_student('Rahul')
# s1.add_teacher('Rajakumari')

# s2 = School('APS')
# s2.add_student('Sumit')
# s2.add_teacher('Ajay')
# s2.add_teacher('Seema')

# s3 = School('St Xavier')
# s3.add_student('Sheetal')
# s3.add_student('Sneha')
# s3.add_teacher('Mohan')
# s3.add_teacher('Priya')
# s3.add_teacher('Amit')

# # Print summaries
# s1.summary()
# s2.summary()
# s3.summary()

# # Change school name using the class-level method
# School.change_school_name('New Modern School')

# # Print summaries after changing school name
# s1.summary()
# s2.summary()
# s3.summary()
