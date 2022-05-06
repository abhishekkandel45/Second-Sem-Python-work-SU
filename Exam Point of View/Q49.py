# Write a python program  to count the number of times a character appears in a string?
a=input("Enter a string: ")
b=input("Enter a character: ")
a=a.lower()
b=b.lower()
c=0
for i in a:
    if i==b:
        c+=1
print (c)
