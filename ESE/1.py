 #Program to find factorail of a number using function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

a= int(input("Enter a number: "))
print("Factorial of",a,"is",factorial(a))
