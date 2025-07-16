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

class animal:

    def __init__ (self, name = "Animal"):
        self.name = name

    def sound(self):
        print(f"{self.name} Sounds.")

class animal_not:
    def __init__ (self, name = "Not Animal"):
        self.name = name

    def not_swim(self):
        print(f"{self.name} can't swim.")

class dog(animal, animal_not):

    def __init__ (self, name = "Dog"):
        self.name = name

    def bark(self):
        print(f"{self.name} barks.")

d = dog("Tony")
d.bark()
d.sound()
d.not_swim()

class test:
    counter = 0

    def __init__ (self):
        self.id = test.counter
        test.counter += 1

class avg:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def average(self):
        return print(f"Average of {self.x} & {self.y} is {(self.x + self.y)/2}. ")
    
a = avg(3,2.4)
a.average()

print(a.x)