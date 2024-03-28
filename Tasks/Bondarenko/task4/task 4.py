max_chr_per_line = int(input("Write maximum number of characters per line (minimum 35)\n"))
prepared_line = ""
new_line = ""
word = ""
lines = []
spaces_left = 0

if max_chr_per_line < 35:
    max_chr_per_line = 35

print("Opening text.txt")
with open("text.txt", "r") as f:
    data = f.read()
    for chr in data:
        if chr != " ":
            word += chr
        if chr == " ":
            if len(prepared_line + word + " ") < max_chr_per_line:
                prepared_line += word + " "
                word = ""
            else:
                prepared_line = prepared_line.strip()
                #print(f"we can add {max_chr_per_line - 1 - len(prepared_line)} spaces to line")

                while len(prepared_line) < max_chr_per_line:
                    spaces_left = max_chr_per_line - len(prepared_line)
                    for i in prepared_line:
                        new_line += i
                        if i == " " and spaces_left > 0:
                            new_line += " "
                            spaces_left -=1
                    prepared_line = new_line
                    new_line = ""

                lines.append(prepared_line)
                prepared_line = word
                word = ""
                spaces_left = 0

with open("new_text.txt", "w") as f:
    for i in lines:
        f.write(i)
        f.write("\n")
print("New file new_text.txt was created")
input("Press enter to exit")



