from sys import *
print(float_info.max)
print(float_info.min)
print(float_info)

large = 2. ** 1021
for i in range(3):
    large *= 2
    print(i, large)