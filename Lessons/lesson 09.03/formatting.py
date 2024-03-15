str1 = "test "
str2 = "not test"

print(str1+str2)
print("test"*8)

c, d, p = 'cat', 'dog', 'parrot'
# "a cat, a dog and a parrot"
print("a " + c + ", a " + d + " and a " + p)
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a parrot"

pattern = "a {}, a {} and a {}"
print("a {}, a {} and a {}".format(c, d, p))
print("a {}, a {} and a {}".format(d, p, c))
print("a {1}, a {2} and a {0}".format(c, d, p))
print("a {cat}, a {dog} and a {parrot}".format(cat=c, dog=d, parrot=p))

print("a", c, ", a", d, " and a", p)

print(f"a {c}, a {d} and a {p}")
x = 25/4.9
print(f"high {x:.0f}")

# print("%s %d" % ("test", 42)) old style, do no use

str1 = "test "
str2 = "not test"
print(f"{str1}{str2}")