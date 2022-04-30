# Wrrite a Python program to find all prime numbers within an interval
a= int(input("Enter the starting point of interval: "))
b= int(input("Enter the ending point of interval: "))
for num in range(a,b+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)