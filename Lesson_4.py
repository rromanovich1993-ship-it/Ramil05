ООП первая часть
class Book:
   GENRETION = "Детектив"

   def __init__(self, page):
       self.page = page

my_book = Book(page=777)
print(my_book.page)