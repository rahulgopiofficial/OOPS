class Bank:
    bank_count = 0

    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        Bank.bank_count += 1
        self.branches = []

    def add(self, b_name):
        self.branches.append(b_name)

    def remove(self, b_name):
        if b_name in self.branches:
            self.branches.remove(b_name)
        else:
            print(f"{b_name} Branch not present in list")


b1 = Bank('Dena', 'Mumbai')
b1.add('Mahape')
b1.add('Kalyan')
b1.add('Thane')
b1.remove('Mahape')

b2 = Bank('ICICI', 'Delhi')
b2.add('Karolbaug')
b2.add('LBS')
b2.add('PM_marg')
b2.remove('PM_marg')
b2.remove('Chandi Chowk')

b3 = Bank('HDFC', 'Bangalore')
b3.add('Hebbal')
b3.add('Whitefeild')
b3.add('HBR Layout')

print(Bank.bank_count)
for i in [b1, b2, b3]:
    print(f"{i.name} has {len(i.branches)} branches and its location is {i.location}, list of branches are {i.branches}")