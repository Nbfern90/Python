class Book():

    favorites = []  # Class attribute = attribute that applies to ALL the CLASSES

    def __init__(self, title, pages):  # constructor, parameter = attributes
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False

    def __str__(self):
        return f"{self.title} is {self.pages} pages long."


book = Book("Cat in the Hat", 72)  # Object or Instance
book2 = Book("Super Fudge", 105)

Book.favorites.append(book)  # adds to the attribute in the CLASS level
Book.favorites.append(book2)

print(Book.favorites)

for b in Book.favorites:
    print(b)


# attributes = What make up the car
# methods-what the car can do
