# with open('test.txt', 'rb') as f:
#     print(repr(f.read()))

# with open('dog.jpg', 'rb') as f:
#     x = f.read(100)
#     print(repr(x), len(x), x)

import time

start = time.time()

chunk_size = 10000000
with open('test.pptx', 'rb') as target:
    with open('test_copy.pptx', 'wb') as copy:
        chunk = True
        while chunk:
            chunk = target.read(chunk_size)
            copy.write(chunk)

end = time.time()

print("the end", end - start)