class Animal:
    is_alive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass

dog = Dog("Doggy")
cat =Cat("Meow")
mouse =Mouse("Chua")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

