class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author= author
        self.pages =pages
        self.price=price
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price-(self.price*self._discount)
        else:
            self.price

    def setdiscount(self, amount):
        self._discount = amount

b1=Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2=Book("The Catcher of rhe Rye", "J D Salinger", 234, 29.95)
print(b1.getprice())
b2.setdiscount(0.25)
print(b2.getprice())