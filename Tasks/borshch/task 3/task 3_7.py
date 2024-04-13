example_string = "A sentence is the largest independent unit of grammar: it begins with a capital letter and ends with a period, question mark, or exclamation point. The word 'sentence' is from the Latin for 'to feel.' The adjective form of the word is 'sentential.' The sentence is traditionally (and inadequately) defined as a word or group of words that expresses a complete idea and that includes a subject and a verb."

# solusion 1 (but it change every entry of a symbol. it's wrong)
# for i in example_string:
    # if i.isupper():
        # example_string = example_string.replace(i, i.lower())
    # if i.islower:
        # example_string = example_string.replace(i, i.upper())
# print(example_string)

# solusion 2
k = list(example_string)
new_string = []
for i in k:
    if i.isupper():
        i = i.lower()
    elif i.islower:
        i = i.upper()
    new_string.append(i)
print("".join(str(new_string).split("', '")).strip("['").strip("']"))