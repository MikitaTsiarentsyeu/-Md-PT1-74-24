
String_length = int(input('Specify a line length of at least 35 characters:\n'))
while String_length < 35:
     String_length = int(input(' Please specify a line length of at least 35 characters:\n'))


with open ('text.txt','r') as oldText:
     oldText = oldText.readlines()

     with open ('text_new.txt','w') as newText:
          for old in oldText:
               old = old.split()
               newline = ''

               for world in old:
               
                    if len(newline) == 0:
                         newline += world
                         continue

                    if len(newline) + len(world) + 1 > String_length:
                         if len(newline) < String_length:
                              t = newline.find(' ')
                              
                              while len(newline) < String_length:
                                   newline = newline[:t] + ' ' + newline[t:]
                                   t += 2
                                   if newline[t:].find(' ') != -1:
                                        t += newline[t:].find(' ')
                                   else:
                                        t = newline.find(' ')

                         newText.write(newline)
                         newText.write('\n')
                         newline = world
                         world = 0

                    while world:
                         if len(newline) < String_length and len(newline) + len(world) <= String_length:
                              newline += ' ' + world
                              world = 0

               newText.write(newline)
               newText.write('\n')
print('New file text_new.txt was created')
