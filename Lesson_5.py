class Human:
    def __init__(self, name):
        self.name = name
        self.famyli = "Испанов"

    def speak(self):
        return f"Человек по имени {self.name} с фамилией {self.famyli} умеет разговаривать"

    def sit(self):
        return f"Человек по имени {self.name} с фамилией {self.famyli} умеет сидеть"

class Dog(Human):
    def paint(self):
        return f"Человек по имени {self.name} с фамилией {self.famyli} умеет рисует"

son = Dog("УФФФ")
print(son.speak())
print(son.paint())