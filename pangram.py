# Write a program to check if a string is a pangram or not
s=input("Enter the string: ")
s=s.lower()
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count=0
for i in alphabets:
    if i in s:
        count+=1
if count==26:
    print("Pangram")
else:
    print("Not a Pangram")
