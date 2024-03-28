file_name = 'text.txt'

try:
    with open(file_name, 'r') as file:
        input_text = file.read()
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    quit()

max_chars_per_line = int(input("Enter maximum number of characters per line (greater than 35): "))
if max_chars_per_line <= 35:
    print("Error: Maximum number of characters per line must be greater than 35.")
    quit()

words = input_text.split()
lines = []
current_line = ''
for word in words:
    if len(current_line) + len(word) <= max_chars_per_line:
        current_line += word + ' '
    else:
        lines.append(current_line.rstrip())
        current_line = word + ' '
lines.append(current_line.rstrip())

justified_lines = []
for line in lines:
    words_in_line = line.split()
    num_words = len(words_in_line)
    if num_words > 1:
        num_spaces_needed = max_chars_per_line - sum(len(word) for word in words_in_line)
        spaces_per_gap = num_spaces_needed // (num_words - 1)
        extra_spaces = num_spaces_needed % (num_words - 1)
        justified_line = ''
        for i in range(len(words_in_line) - 1):
            justified_line += words_in_line[i] + ' ' * (spaces_per_gap + 1 if i < extra_spaces else spaces_per_gap)
        justified_line += words_in_line[-1]
        justified_lines.append(justified_line)
    else:
        justified_lines.append(line)

output_text = '\n'.join(justified_lines)

print("Debug: Output text before writing to file:")
print(output_text)  

output_file_name = 'justified_text.txt'
with open(output_file_name, 'w') as output_file:
    output_file.write(output_text)

print(f"Justified text has been written to '{output_file_name}'.")
