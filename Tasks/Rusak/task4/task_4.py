def justify_text(input_file, output_file, max_characters_per_line):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        words = content.split()
        lines = []
        current_line = ''

        for word in words:
            if len(current_line) + len(word) <= max_characters_per_line:
                current_line += word + ' '
            else:
                lines.append(current_line.strip())
                current_line = word + ' '
        
        # Add the last line
        lines.append(current_line.strip())

        justified_lines = []

        for line in lines:
            words_in_line = line.split()
            if len(words_in_line) > 1:
                num_gaps = len(words_in_line) - 1
                total_spaces_needed = max_characters_per_line - len(line)
                spaces_between_words = total_spaces_needed // num_gaps
                extra_spaces = total_spaces_needed % num_gaps

                justified_line = ''
                for i in range(len(words_in_line) - 1):
                    justified_line += words_in_line[i] + ' ' * spaces_between_words
                    if extra_spaces > 0:
                        justified_line += ' '
                        extra_spaces -= 1

                justified_line += words_in_line[-1]
                justified_lines.append(justified_line)
            else:
                justified_lines.append(line)

        with open(output_file, 'w') as f:
            f.write('\n'.join(justified_lines))

        print("Text has been justified and written to", output_file)

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    max_characters_per_line = int(input("Enter the maximum number of characters per line (greater than 35): "))

    if max_characters_per_line <= 35:
        print("Maximum number of characters per line must be greater than 35.")
    else:
        justify_text(input_file, output_file, max_characters_per_line)
