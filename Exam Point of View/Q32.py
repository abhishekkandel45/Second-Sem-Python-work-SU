# Python prohrom to seach a given string from a listof sting using loop
a=input("Enter a string: ")
b=["John","Mary","Bob","Alice"]
for i in b:
    if a==i:
        print ("Found it at index: ",b.index(i))
        break
else:
    print ("Not found")