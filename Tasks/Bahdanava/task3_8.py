#First option

x = [1, 3, 2, 5, 6, 7, 8, 10]
average = sum(x) / len(x)
print(average)

#Second option

import statistics

x = [1, 3, 5, 2, 6, 8, 10]
average = statistics.mean(x)
print(average)