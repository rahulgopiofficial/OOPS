class library:
    def __init__(self, books, members):
        self.books = books
        self.members = members

    def add_books(self, book):
        self.books.append(book)
    
    def remove_books(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print('Book not present')

    def add_member(self, member):
        self.members.append(member)
    
    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print('Member not present')

    def show(self):
        print(self.books, self.members)

l1 = library(["Danvinci code", "ITHALS", "Alladin"], ['Rahul', 'Arsalan', 'Ramesh'])

l1.add_books('APJ')

l1.remove_books('ITHALS')

l1.add_member('Midhun')

l1.remove_member('Arsalan')

l1.show()