# To find the factorial of given number using Function.
def factorial(n):
    if n==1:
        return 1
    else:
        fact=n*factorial(n-1)
        return fact
num=int(input("Enter the number: "))
print(factorial(num))
