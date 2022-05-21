# Factorial of any number n is repersnted by n! and is 1*2*3*...*(n-1)
#eg: 4!=1*2*3*4=24
#3!=1*2*3=6
#2!=1*2=2
#Also, 1!=1 and 0!=1
# Write a program to find the factorial of a number
n= int(input("Enter the number"))
fact=1
for i in range (1, n+1):
    fact=fact*i
print ("Factorial of ", n, "is", fact)