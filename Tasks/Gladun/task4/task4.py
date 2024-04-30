user_input_length = int(input("Please, input line length(min 35): "))
if user_input_length < 35:
    user_input_length = 35
line = ""
line_finale = ""
words = ""
line_k = []
space_left = 0

with open('text.txt', 'r') as sample:
    line_sample = sample.read()

    with open('text_redact.txt', 'w') as result:
        for sbl in line_sample:
            if sbl != " ":
                 words += sbl
            if sbl == " ":
                if len(line + words + " ") < user_input_length:
                    line += words + " "
                    words = ""
                else:
                    line = line.strip()
                    while len(line) < user_input_length:
                        space_left = user_input_length - len(line)
                        for i in line:
                            line_finale += i
                            if i == " " and space_left > 0:
                                line_finale += " "
                                space_left -= 1
                        line = line_finale
                    line_k.append(line_finale)
                    line = words + " "
                    words = ""
                    line_finale = ""

        for i in line_k:
            result.write(i)
            result.write("\n")
