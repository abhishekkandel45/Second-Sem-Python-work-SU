# Write a python program to seprate punctuation marks from the string and print the punctuation marks separately? Space is not considered as punctuation mark.
a=input("Enter a string: ")
b=[]
c=[]
d=[]
for i in a:
    if i.isalpha():
        c.append(i)
    elif i.isdigit():
        b.append(i)
    elif i.isspace():
        pass
    else:
        d.append(i)
print ("Letters: ",c)
print ("Numbers: ",b)
print ("Punctuation: ",d)