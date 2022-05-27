#Write a program using a user defined function that displays sum of first n natural numbers, where n is passed as an argument.
def sumnat(n):
    sum=0
    for i in range (1,n+1):
        sum += i
    return sum
n=int(input("Enter the number:"))
print("The sum of first",n,"natural numbers is",sumnat(n))

        