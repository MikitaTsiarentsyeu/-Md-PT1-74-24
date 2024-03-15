# есть какое-то математическое выражение, например, пользователь с консоли может его ввести, но можешь для решения
# просто хранить пример выражения в программе, что-то в стиле '((2+5)*3)/(8-6)', и тебе нужно написать функцию,
# которая будет проверять, правильно ли расставлены скобки в этом выражении(то есть нет ли пропущенных или лишних)

def check_brackets_count(math_data):
    right_bracket = [i for i in range(len(math_data)) if math_data[i] == ')']
    left_bracket = [i for i in range(len(math_data)) if math_data[i] == '(']
    if len(right_bracket) % 2 == 0:
        print("Invalid data: check count of symbol ')'")
    elif len(left_bracket) % 2 == 0:
        print("Invalid data: check count of symbol '('")


check_brackets_count(math_data=input("Enter math data in string format: "))
