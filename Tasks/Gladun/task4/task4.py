user_input_length = int(input("Please, input line length(min 35): "))
if user_input_length < 35:
    user_input_length = 35
line = ""
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
                    if len(line) < user_input_length:
                        space_left = user_input_length - len(line)
                        s = line.find(" ")
                        while len(line) < user_input_length:
                            line = line[:s] + " " + line[s:]
                            s += 2
                            if line[s:].find(' ') != -1:
                                s += line[s:].find(' ')
                            else:
                                s = line.find(' ')
                    result.write(line)
                    result.write('\n')
                    line = words + " "
                    words = ""