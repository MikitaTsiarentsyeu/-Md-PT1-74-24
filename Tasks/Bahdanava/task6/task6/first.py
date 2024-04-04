def reverse_string(a):
    if len(a) == 0:
        return a
    else:
        return reverse_string(a[1:]) + a[0]

input_string = "Hello, world"
reversed_string = reverse_string(input_string)
print("Reversed string: ", reversed_string)
