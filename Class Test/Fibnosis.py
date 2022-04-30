#write a python Program to find the Fibonacci series upto n terms using interation
a= int(input("Enter the number of terms"))
b=0
c=1
print(b,c,end=" ")
for i in range(2,a):
    d=b+c
    print(d,end=" ")
    b=c
    c=d
print()
