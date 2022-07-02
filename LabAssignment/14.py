# To Print fibonisaci series using function.
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number of terms: "))
print("The first",n,"terms of the fibonacci series are: ")
for i in range(1,n+1):
    print(fibonacci(i), end=" ")
    