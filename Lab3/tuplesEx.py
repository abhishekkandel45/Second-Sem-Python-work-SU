#write a program to create tuple whose elements and size are given by user

size = int(input("Enter the size of tuple: "))
tuple = ()
for i in range(size):
    ele = int(input("Enter the element: "))
    tuple = tuple + (ele,)
print(tuple)
