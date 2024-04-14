# Func count character

def func_count_charac(text,char):
    if text.find(char) >= 0:
        return 1 + func_count_charac(text[(text.find(char))+1:], char)
    else:
        return 0


b = 'Hello Hello'
print(func_count_charac(b,'l'))
