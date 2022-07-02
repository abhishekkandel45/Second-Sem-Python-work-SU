# To print n terms  of the fibonacci series using interative method.
terms=int(input("Enter the number of terms: "))
n1=0
n2=1
count=0
if terms<=0:
    print("Please enter a positive integer")
elif terms==1:
    print(n1)
else:
    print(n1,n2, end=" ")
    while count<terms-2:
        n3=n1+n2
        print(n3, end=" ")
        n1=n2
        n2=n3
        count= count+1
        