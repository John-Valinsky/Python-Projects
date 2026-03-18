Polymorphism
============
class Bird:
    def fly(self):
        print("Bird flies")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Bird()
p = Penguin()

b.fly()
b.fly()
