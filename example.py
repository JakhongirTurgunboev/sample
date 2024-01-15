class Book:
    def __init__(self, name, publish, author):
        self.name = name
        self.publish = publish
        self.author = author


class Author:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date


author1 = Author('J.K.Rowling', 'UK', 1970)

book1 = Book('Harry Potter', 1995, author1)
book2 = Book('Harry Potter 2', 2000, author1)

print(book1.name, book1.publish, book1.author.name, book1.author.country, book1.author.birth_date)

print(book2.name, book2.publish, book2.author.name, book2.author.country, book2.author.birth_date)
