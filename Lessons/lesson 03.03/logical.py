print(True, False, type(True), type(False))

print(1 == True, 0 == False)
print(True+True+True+False)

print(bool(65346), bool(-5346), bool(0.0), bool(0.000000000001))
print(bool(float('inf')), bool(float('nan')))

print(bool(bool), bool(print))

print(bool(''), bool([]), bool(None))
print(type(None))

res = print("test print")
print(res)

print(not 45, not False, not print, not '')

print(True and True)
print(False or True)
print(True or False)

print(4 or 5)
print(4 and 5)

print(0 and print("the right part"))
print(0 or print("the right part"))


x = 5
print(x > 10)