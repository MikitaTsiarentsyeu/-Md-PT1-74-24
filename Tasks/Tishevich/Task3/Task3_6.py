# 6. Write a program that takes a string as input and returns the string with all vowels removed.
def delete_vowels_in_string(user_string):
    update_string = ''.join(x for x in user_string if x not in 'eyuioaуеыаоэяиюEYUIOAEAOЮЕЭЯИЫЯУОА')
    print(update_string)


delete_vowels_in_string(user_string=input("Enter your data: "))
