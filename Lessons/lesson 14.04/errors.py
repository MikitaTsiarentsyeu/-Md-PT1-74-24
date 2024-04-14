l = []

def test_func():
    try:
        raise RuntimeError("something went wrong")
        print(l[0])
        print("test")
    except (NameError, KeyError):
        print("wrong variable name")
    except IndexError:
        print("wrong index value")

try:
    print("before call")
    test_func()
    print("after call")
except RuntimeError as e:
    print(e)
    try:
        raise TypeError("OOOOPS!")
    except:
        pass
except:
    print("something went wrong")

print("the main logic goes here")


try:
    is_open = False
    f = open("test.txt", 'r')
    is_open = True
    f.write("test")
    raise RuntimeError("something went wrong with the file")
except RuntimeError as e:
    print(e)
finally:
    if is_open:
        f.close()
    print("file is closed")