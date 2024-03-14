# Unicode
# ASCII

print(ord('A'), ord('a'))
print(ord('А'), ord('а'))
print(ord('🙂'))

print(chr(65), chr(650), chr(6500), chr(11000))
print(chr(128578), chr(128579), chr(128580))

t1 = "test"
t2 = 'test'
print(t1 == t2)

"Hello, I'm Python"
'Hello, I"m Python'
'Hello, I\'m Python'

print("\tline1\nline2")
# t = input()
# print(repr(t))

t1 = "test"
t2 = 'test'
# print(t1 == t2)
t3 = '''test'''
t4 = """test"""
print(t1 == t2 == t3 == t4)

"test\ntest"

test = """     line1
        line2
        line3"""
print(test)
print(repr(test))


my_test_str = "my very long string"
print(len(my_test_str), len(' '), len('\n'), len(''))
print(my_test_str[0], my_test_str[1], my_test_str[2], my_test_str[3], my_test_str[4])
# print(my_test_str[100]) error
print(my_test_str[0], my_test_str[-1], my_test_str[-2], my_test_str[-3], my_test_str[-4])
print(my_test_str[len(my_test_str)-1])

print(repr(my_test_str[0:7]))
print(repr(my_test_str[:7]))
print(repr(my_test_str[3:]))
print(repr(my_test_str[:]))

print(repr(my_test_str[3:-3]))
print(repr(my_test_str[3:-3:2]))
print(repr(my_test_str[::-1]))

# print(s == s[::-1])

print('s' in my_test_str)
print('test' in my_test_str)
print('string' in my_test_str)

print(my_test_str.find('s'))
print(my_test_str.find(' '))
print(my_test_str.find('very'))
print(my_test_str.find('test'))

# my_test_str[0] = 'M'
print(my_test_str.replace('m', 'M'), my_test_str)
print(my_test_str.replace('n', 'N'), my_test_str)
my_test_str = my_test_str.replace('m', 'M').replace(' ', '_').replace('very', '')
print(my_test_str)
print(my_test_str.upper().lower().capitalize())

s = "my test string"
print(s.split())
s = "435_%APAC"
print(s.split('_%'))

s = "!my! !test! !string!"
s.replace('!', '')
print(' '.join(s.split('! !')).strip('!'))