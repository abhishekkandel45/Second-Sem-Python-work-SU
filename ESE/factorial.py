# Factorial using recursion and without recursion
def factorial_without_recursion(num):
    if num==0:
        return 1
    else:
        return num*factorial_without_recursion(num-1)

def factorial_with_recursion(num):
    if num==0:
        return 1
    else:
        return num*factorial_with_recursion(num-1)