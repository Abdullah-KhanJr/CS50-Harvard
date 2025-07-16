class person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def greet(self):
        print(f"Hello {self.n}, your age is {self.a}.")

p = person("Abdullah", 21)
p.greet()


p = person("john", 32)
p.greet()


class car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "started")

my_car = car("Toyota")
my_car.start()

class student:
    def __init__ (self, name = "Unkown"):
        self.name = name

    def marks(self):
        print(f"{self.name} scored 20 marks.")

s = student("Abdullah")
s.marks()

