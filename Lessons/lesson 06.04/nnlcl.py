
def test_global():
    global global_var

    global_var = "test"

test_global()
print(global_var)

def test_local_outer():
    outer_var = "outer"
    print(outer_var)
    def test_local_inner():
        nonlocal outer_var
        outer_var = "inner"
        print(outer_var)
    test_local_inner()
    print(outer_var)

test_local_outer()