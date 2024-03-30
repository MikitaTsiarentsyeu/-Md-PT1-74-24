MY_FILE = 'text.txt'
NEW = 'new_file.txt'
max_chars = int(input('Enter the maximum numbers per characters '
                      '(greater than 35):\n'))

start = 0

try:
    with open(MY_FILE, 'r') as f:
        with open(NEW, 'w') as new:
            content = f.read()
            for symbol in content:
                    if symbol == chr(226) or symbol == chr(8364) or symbol == chr(8482):
                        content = content.replace(symbol, "'")
                        content = content.replace("'''", "'")
            line = True
            while line:
                line = content[start:(start + max_chars + 1)]
                if len(line) < max_chars:
                    new.write(line)
                    break
                elif '\n' in line:
                    ind_transfer = line.find('\n')
                    line = content[start:(start + ind_transfer + 1)]
                    new.write(line)
                    start += len(line)
                elif not line.endswith(' '):
                    ind_space = line.rfind(' ')
                    line = content[start:(start + ind_space)]
                    start += ind_space + 1
                    neces_space = True
                    while neces_space:
                        neces_space = max_chars - len(line)
                        line = line.replace(' ', '  ', neces_space)
                        neces_space = max_chars - len(line)
                        if neces_space != 0:
                            neces_space = True
                        else:
                            neces_space = False
                    new.write(f'{line}\n')
                else:
                    new.write(f'{line.rstrip(' ')}\n')
                    start += len(line)
            print(f'The formatted text was written to the {NEW} file')
except:
    print("The file was not found or the recording could not be performed.")
