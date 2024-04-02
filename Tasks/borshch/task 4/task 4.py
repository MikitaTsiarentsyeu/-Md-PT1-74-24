user_input = int(input("please, enter maximum symbols per line: \n"))

with open("text.txt", "r") as f:
    words = f.read().split(" ")

line = ""
new_lines = []
for word in words:
    if (len(line) + len(word)) <= user_input:
        if "\n" in word:
            word_1, word_2 = word.split("\n")
            line += (word_1 +"\n")
            new_lines.append(line)
            line = word_2 + " "
        else:
            line += (word + " ")
    else:
        if "\n" in word:
            word_1, word_2 = word.split("\n")
            if (len(line) + len(word_1)) <= user_input:
                line += (word_1 +"\n")
                new_lines.append(line)
                line = word_2 + " "
        else:
            line = line.strip(" ") + "\n"
            new_lines.append(line)
            line = word + " "
    if word == words[-1]:
        new_lines.append(line)

extra_spaces_needed = 0
for i in range(len(new_lines)):
    while len(new_lines[i]) <= user_input:
        extra_spaces_needed = user_input - len(new_lines[i])
        l = new_lines[i].split(" ")
        for j in range(len(l)):
            if j == len(l) -1:
                continue
            elif j in range(extra_spaces_needed + 1):
                l[j] += "  "
            elif j in range(extra_spaces_needed, len(l)-1):
                l[j] += " "

        new_lines[i] = "".join(l)
        if len(new_lines[i]) == user_input +1:
            break

user_answer = input("do you want to write the text according your maximum symbols per line to a new file?\n Y/N:")
if user_answer == "Y":
    with open("new text.txt", "w") as b:
        b.writelines(new_lines)
if user_answer == "N":
    quit()
print(new_lines)
