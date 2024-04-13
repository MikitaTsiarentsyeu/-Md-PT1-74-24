user_input_string = str(input("Please, enter your string"))

m = list(user_input_string)

print("".join(str(m[ : :-1]).split("', '")).strip("['").strip("']"))
