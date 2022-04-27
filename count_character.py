# Write a program to count the number of characters repeated in a string.
string = input("Enter the string: ")
count = {}
for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)
