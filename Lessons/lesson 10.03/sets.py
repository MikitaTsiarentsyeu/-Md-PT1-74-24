s = {1, 2, 3, 3, 3, 3}
print(s, type(s), len(s))

s = {}
print(s, type(s), len(s))

s = set()
print(s, type(s), len(s))

s = set("test string ")
print(s)

print("test string test" == "test string")
print(set("test string test") == set(['g', ' ', 't', 'n', 'r', 'i', 's', 'e']))

s.add("test")
print(s)

s.remove("test")
print(s)

if "test" in s:
    s.remove("test")
    print(s)

s.clear()
print(s)

print({1,2,3}.union({3,4,5}))
print({1,2,3}.intersection({3,4,5}))