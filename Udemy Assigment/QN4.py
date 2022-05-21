# Write a Python Program to calculate the sum and average og n intergers numbers:
n= int(input("Enter the integers numbers"))
sum=0
for i in range (1, n+1):
    sum=sum+i
print ("Sum =", sum)
average= sum/n
print("Avegrage =", average)    