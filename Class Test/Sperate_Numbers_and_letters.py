#write a program to seprarte numbers and letters from the given string.
a= input("Enter the string: ")
b=[]
c=[]
for i in a:
    if i.isdigit():
        b.append(i)
    else:
        c.append(i)
print ("The numbers are: ",b)
print ("The letters are: ",c)           
