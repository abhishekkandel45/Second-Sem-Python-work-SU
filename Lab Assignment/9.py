# to find all the prime mumber in the given range.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num1,num2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i, end=" ")
            