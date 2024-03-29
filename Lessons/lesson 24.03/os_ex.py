import os

print(os.getcwd())

# open('test.txt', 'w')
# open('C:\\Drive D\\Projects\\IT Academy\\Python\\Md-PT1-74-24\\repo\\Lessons\\lesson 24.03\\test.txt', 'w')
open(r'C:\Drive D\Projects\IT Academy\Python\Md-PT1-74-24\repo\Lessons\lesson 24.03\test.txt', 'w')

# print(os.name)

# sep = '\\' if os.name == 'nt' else '/'

print(os.sep)

print(os.sep.join(['level 1', 'level 2', 'level 3']))

new_dirs = os.path.join('level 1', 'level 2', 'level 3')
print(new_dirs)

# os.mkdir("test\\test") only for one dir

# os.makedirs(new_dirs) for nested dirs

# os.chdir(new_dirs)
# print(os.getcwd())

# open("new_text.txt", 'w')

print(os.listdir())

for p in os.walk(os.getcwd()):
    print(p)

os.remove(os.path.join(new_dirs, "new_text.txt"))
os.removedirs(new_dirs)