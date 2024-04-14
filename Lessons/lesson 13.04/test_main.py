test_additional = "test_additional"

print(test_additional)

import test_additional as test_add
from test_additional import test_func as add_test_func, test_list as add_test_list
from test_additional import *

print(type(test_add), test_add)
# print(test_additional.__dict__)

print(test_add.test_text)
print(test_add.test_list)

test_add.test_func()

test_add.test_text = "new text"
test_add.test_list.append("new elem")

test_add.show_test_text()
test_add.show_test_list()

test_additional = "new value"
print(test_additional)

add_test_func()

print(__name__)