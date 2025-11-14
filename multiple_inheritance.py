class Animal:
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This Animal is sleeping")

class Prey(Animal):
    def flee(self):
        print("This Animal is sleeping")

class Predator(Animal):
    def hunt(self):
        print("This Animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()