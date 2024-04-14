# import time_it

# time_it = time_it.Time_it()

from time_it import Time_it

time_it_outer = Time_it()
time_it_inner = Time_it()

time_it_outer.start()
for i in range(100000):
    time_it_inner.start()
    for j in range(100000):
        i+j
    print(time_it_inner.finish())
time = time_it_outer.finish()
print(time)