        # OOP часть первая
    # Создатим класс книги (класс это шаблон для создания объекта)
class Book:
# у класса могут общие атрибуты (они пишутся с большой буквы)
# выводим общий атрибут (его можно использовать у всех объектов)
    GENRE  = "Детектив"
    GENRE1 = "Роман"
    GENRE3 = "Фантастика"
# создаём объект ,нужно давать описательное название
    def __init__(self,page):
        self.page = page
my_book = Book(page=1)
# Теперь мы можем обратится и вызвать данный атрибут
print(my_book.page)

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Имя:{self.name}, возраст: {self.age}")

human1 = Human(name="Ramil",age=20)
human1.info()
human2 =Human(name="Alex",age=30)
human2.info()





