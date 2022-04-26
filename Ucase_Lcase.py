#Write a program to calculate the number of upper case letters and lower case letters in a string
s=input("Enter the string: ")
count_upper=0
count_lower=0
for i in range(len(s)):
    if s[i].isupper():
        count_upper+=1
    elif s[i].islower():
        count_lower+=1
print("The number of upper case letters are: ",count_upper)
print("The number of lower case letters are: ",count_lower)
