#1
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

abc = BankAccount(20974104, 389543.22)
print("Current balance is:", abc.balance)

deposit = float(input("Enter the amount to deposit"))
new_balance = abc.balance + deposit

print("Current balance is:", new_balance)



#2
class student:
    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade

    def update_grade(self, newgrade):
        self.grade = newgrade

s1 = student('Rahul', 100)

print(f"Student name is {s1.name} and old grade {s1.grade}")

s1.update_grade(150)

print(f"Student name is {s1.name} and new grade {s1.grade}")