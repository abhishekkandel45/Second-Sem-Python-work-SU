# Python program to Reverse a Number and find the sum of its digits
n=int(input("Enter a number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number is: ",rev)
sum=0
while(rev>0):
    dig=rev%10
    sum=sum+dig
    rev=rev//10
print("Sum of the digits is: ",sum)
