class bankaccount:
    def __init__(self, acc_no, acc_name, balance) -> None:
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -=amount
        else:
            print("Insufficient Balance !!!")
    
    def display(self):
        print(f"{self.acc_name}, your account no {self.acc_no} has a balance of {self.balance} Rs")

u1 = bankaccount(123456, "Rahul", 40000)
u1.display()
u1.deposit(5000)
u1.display()
u1.withdraw(20000)
u1.display()
u1.withdraw(30000)



class product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalcost(self):
        return self.price * self.quantity
    

p1 = product('Wheat', 500, 34)
print(p1.totalcost())