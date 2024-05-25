

class Lightning:

    power = 1000000

    def struck(self, tree):
        tree.burn()

class Tree:

    age = 100

    def get_struck(self, lightning):
        lightning.struck(self)

    def burn(self):
        print("burning...")

l = Lightning()
t = Tree()

# l.struck(t)
t.get_struck(l)



class PetDog:

    # name = ""
    # __breed = "shepherd"
    # happines_level = 100
    # favorite_food = "everything"

    def __init__(self, name, breed, color, age, happines_level=100, favorite_food="meat"):
        self.name = name
        self.__breed = breed
        if breed == "wss":
            self.__color = "white"
        else:
            self.__color = color
        self.__set_age(age)
        self.set_happines_level(happines_level)
        self.favorite_food = favorite_food

    def __set_age(self, age):
        if age > 0 and age < 30:
            self.__age = age
        else:
            self.__age = 0

    def update_age(self):
        self.__age += 1

    def get_age(self):
        return f"{self.__age} year(s)"

    def set_happines_level(self, new_value):
        if new_value < 101 and new_value > 0:
            self.__happines_level = new_value
        else:
            self.__happines_level = 50

    def get_happines_level(self):
        return f"{self.__happines_level}%"


    happines_level = property(get_happines_level, set_happines_level)


dog = PetDog("Zephirka", "wss", "black", 3)

print(dog.name)
print(dog.get_age())
dog.update_age()
# print(dog._PetDog__age)
print(dog.get_age())

print(dog.happines_level)
dog.happines_level = 88
print(dog.happines_level)