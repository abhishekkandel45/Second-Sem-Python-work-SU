# Write a python script to generate a list at runtime.
import random
list = []
for i in range(10):
    list.append(random.randint(1, 100))
print(list)

