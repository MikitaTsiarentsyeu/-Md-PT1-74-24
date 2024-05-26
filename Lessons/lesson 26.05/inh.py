
class A:

    attr = "A attr"

    def test(self):
        print("this is A class")

class B(A):

    def new_method(self):
        print("new method of B")

    def test(self):
        print("this is B class")

# print(A.__dict__)
# print(B.__dict__)

b = B()
# print(b.attr)
# b.test()
# b.new_method()


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")



class Dog(Animal):

    def __init__(self, name, breed, color):
        super().__init__(name)
        self.breed = breed
        self.color = color

    def hunt(self):
        print("hunting")

d = Dog("Zephirka", "wss", "white")

d.sleep()


class SwimingAnimal(Animal):

    def move(self):
        print("I'm swiming")

class FlyingAnimal(Animal):

    def move(self):
        print("I'm flying")

class RunningAnimal(Animal):

    def move(self):
        print("I'm running")


class Dog(RunningAnimal, SwimingAnimal):

    pass

# d = Dog()
# d.run()
# d.swim()

class Duck(FlyingAnimal, RunningAnimal, SwimingAnimal, Animal):

    pass

d = Duck("ducky")
d.move()


print(Duck.mro())
