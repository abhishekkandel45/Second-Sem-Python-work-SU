# Write a program to print the Fibonacci series  using interation.

a=int(input("Enter the number of terms: "))
n1=0
n2=1
count=0
if a<=0:
    print("Please enter a positive integer")
elif a==1:
    print(n1)
    print
else:
    print(n1,n2,end="  ")
    while count<a-2:
        nth=n1+n2
        print(nth, end="  ")
        n1=n2
        n2=nth
        count+=1
