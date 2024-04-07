# class Simpleton:
#     test_atr = "TEST"

#     def test_method():
#         print("TEST!")

# print(type(Simpleton), Simpleton)


class Dog:

    color = ""
    breed = ""
    name = ""

    def bark(self):
        print("BARK!")

    def get_dirty(self):
        if self.color == "white":
            print("You will clean me all day!")
        else:
            print("It's OK")

print(Dog)
print(Dog.name, Dog.color)
# Dog.bark()


zefirka = Dog()
print(zefirka, type(zefirka))

# print(zefirka.color)
zefirka.color = "white"
zefirka.breed = "wss"
zefirka.name = "zefirka"

print(zefirka.color, zefirka.breed, zefirka.name)

print(Dog.color, Dog.breed, Dog.name)

boy = Dog()
boy.color = "black"
boy.breed = "shepherd"
boy.name = "boy"

print(boy.color, boy.breed, boy.name)


# Dog.bark()
zefirka.bark()
boy.bark()

zefirka.get_dirty()
boy.get_dirty()