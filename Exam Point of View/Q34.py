# Python Program to seprate numbers and letters from the string
a=input("Enter a string: ")
b=[]
c=[]
for i in a:
    if i.isdigit():
        b.append(i)
    else:
        c.append(i)
print ("Numbers: ",b)
print ("Letters: ",c)
