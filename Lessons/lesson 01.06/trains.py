class FreightTrain:

    def __init__(self, cart_count):
        self.__carts = [None for i in range(cart_count)]
        self.cart_count = cart_count

    def __eq__(self, value: object):
        # if not isinstance(value, FreightTrain):
        #     return False
        
        try: 
            return self.cart_count == value.cart_count
        except AttributeError:
            return False
        
    def __str__(self):
        return f"{FreightTrain.__name__}({self.cart_count})"
    
    def __int__(self):
        return self.cart_count 
    
    def __add__(self, value):
        if isinstance(value, FreightTrain):
            return FreightTrain(self.cart_count + value.cart_count)
        elif isinstance(value, int) or isinstance(value, float):
            return value + self.cart_count
    
        raise TypeError(f"cannot add non-{FreightTrain.__name__} objects")
    
    def __len__(self):
        return self.cart_count

    def __iter__(self):
        self.__iter_index = 0
        return self
    
    def __next__(self):
        if self.__iter_index >= self.cart_count:
            del self.__iter_index
            raise StopIteration
        else:
            item = self.__carts[self.__iter_index]
            self.__iter_index += 1
            return item
        
    def __getitem__(self, key):
        try:
            return self.__carts[key]
        except IndexError:
            raise IndexError("Cart number is out of range")
        
    def __setitem__(self, key, value):
        try:
            self.__carts[key] = value
        except IndexError:
            raise IndexError("Cart number is out of range")


class Stub: pass

one = FreightTrain(5)
two = FreightTrain(5)
s = Stub()
s.cart_count = 5

print(one == two)
print(one == one)
print(one == s)

print(one)
print(int(one))
# print(10 + one)

print(one+two)
print(one+1.5) # one.__add__(1.5)
# print(1.5+one) # 1.5.__add__(one)

print(len(one))
for i in one:
    print(i)

print(one[1])
one[1] = "test"
print(one[1])

for i in one:
    print(i)
