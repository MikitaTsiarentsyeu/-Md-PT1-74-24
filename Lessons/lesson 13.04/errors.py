l = []

try:
    print(l[0])
    print("test")
except NameError:
    print("wrong variable name")
except IndexError:
    print("wrong index value")
except:
    print("something went wrong")

print("the main logic goes here")