def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        fact=n*(n-1)
        return fact

a=int(input("Enter the number: "))
print("The Factorial is", factorial(a))       