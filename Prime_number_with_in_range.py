# Wrte a  Python Program to find all the prime numbers with in a given range.

a=int(input("Enter the starting number: "))
b=int(input("Enter the ending number: "))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
            