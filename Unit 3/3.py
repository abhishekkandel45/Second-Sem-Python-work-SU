#Write a program using user defined function that accepts an integer and increments the value by 5. 
# #Also display the id of argument (before function call), id of parameter before increment and after increment.
def increment(x):
    x=x+5
    print("id of argument before function call:",id(x))
    print("id of parameter before increment:",id(x))
    print("id of parameter after increment:",id(x))
    return x
x=int(input("Enter the number:"))
print("The value after increment is",increment(x))