

class Food:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __str__(self):
        return self.name
    

class Animal:

    food_kinds = []

    def eat(self, something, breaking=False):
        if breaking:
            print(f"eating {something}")
        else:
            self.phe()

    def phe(self):
        print("phe...")


class Carnivore(Animal):

    food_kinds = ["meat"]

    def eat(self, something):
        if something.kind in Carnivore.food_kinds:
            Animal.eat(self, something, True)
        else:
            super().eat(something)


class Herbivore(Animal):

    food_kinds = ["herbal"]

    def eat(self, something):
        if something.kind in Herbivore.food_kinds:
            Animal.eat(self, something, True)
        else:
            super().eat(something)

class Omnivore(Carnivore, Herbivore): pass

    # def eat(self, something):
    #     if something.kind == "meat":
    #         Carnivore.eat(self, something)
    #     elif something.kind == "herbal":
    #         Herbivore.eat(self, something)
    #     else:
    #         Animal.phe()


steak = Food("steak", "meat")
grass = Food("grass", "herbal")

c = Carnivore()
h = Herbivore()
o = Omnivore()

print(Omnivore.mro())
o.eat(steak)
o.eat(grass)