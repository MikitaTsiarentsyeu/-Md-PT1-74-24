# with open("target_file.txt", 'r') as f:
#     content = f.read()
#     print(content)

# content += " "
# signs = '!', '?', '...', '.'
# sep = '%%%'
# for sign in signs:
#     content = content.replace(sign+' ', sep)

# content = [x+'\n' for x in content.split(sep) if x]

# with open("target_file_copy.txt", 'w') as f:
#     f.writelines(content)


signs = '!', '?', '...', '.'

with open("target_file.txt", 'r') as target:
    with open("target_file_copy.txt", 'w') as new:
        symbol = True
        skip = False
        last = ''
        while symbol:
            symbol = target.read(1)
            if skip:
                skip = False
                continue
            if symbol in signs:
                if last != '\n':
                    new.write('\n')
                    last = '\n'
                    skip = True
            else:
                new.write(symbol)
                last = symbol