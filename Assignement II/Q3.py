# Q3. Write Python Program to count the number of characters in a string using dictionaries. Display the and their values in alphabetical Order.
string=input("Enter a string: ")
d={}
for i in string:
    d[i]=string.count(i)
print(d)
print(sorted(d.items()))


#or
string=input("Enter a string: ")
d={}
for i in string:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
print(sorted(d.items()))
