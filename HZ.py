from math import trunc


class Cat:
    name = None
    age = None
    isHappy = None
    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def speak(self):
        print(self.name, self.age), print(self.isHappy)

cat1 = Cat("Юарсик", 23, True)
cat2 = Cat("Юарсик", 25, False)
cat1.speak()
cat2.speak()