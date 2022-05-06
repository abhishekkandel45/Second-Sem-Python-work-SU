# Python program to check whether a number is prime or not using for loop
a=int(input("Enter a number: "))
for i in range(2,a):
    if a%i==0:
        print ("Not a prime number")
        break
else:
    print ("Prime number")
