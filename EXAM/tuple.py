size = int(input("Enter the size of tuple: "))
tuple = ()
for i in range(size):
    ele = int(input("Enter the element: "))
    tuple = tuple + (ele,)
print(tuple)
