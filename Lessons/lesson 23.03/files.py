# f = open("test.txt", 'w')
# print(type(f), f)

# f.close()

with open("test.txt", 'w') as f:
    f.write("test line 1\n")
    f.write("test line 2\n")
    # f.writelines(["line 3", "line 4", "line 5"])



with open("test.txt", 'r') as f:
    # print(f.read())
    # lines = f.readlines()
    # print(lines)
    for line in f:
        print(repr(line))

with open("test.txt", 'a') as f:
    f.write("new line from 'a'\n")

with open("test.txt", 'a+') as f:
    f.write("new line from 'a+'")
    f.seek(0)
    print(repr(f.read()))
    f.seek(0)
    f.write("writing from the beggining???")

with open("test.txt", 'r+') as f:
    # print(repr(f.read()))
    f.write("new content from r+")
    print(repr(f.read()))

with open("test.txt", 'w+') as f:
    print(repr(f.read()))
    f.write("new line from w+\n")
    print(repr(f.read()))
    f.seek(0)
    print(repr(f.read(5)))
    f.write("overwriting this file")