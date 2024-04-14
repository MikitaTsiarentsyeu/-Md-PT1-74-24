# import test_main - bad approach

# print(__name__)

test_text = "some text value"

test_list = [1,2,3,4,5]

def test_func():
    print("this is test func")

if __name__ == "__main__":
    print(test_text)


def show_test_list():
    print(test_list)

def show_test_text():
    print(test_text)
