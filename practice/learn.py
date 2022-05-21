#write program to check the string is palindrome or not
str1 = input("Enter the string: ")
str2 = str1[::-1]
if str1 == str2:
    print("The string is palindrome")
else:
    print("The string is not palindrome")



#Write a program to remove punctuations from a string
str1 = input("Enter the string: ")
str2 = ""
for i in str1:
    if i not in "!@#$%^&*()_+-=[]\{}|;':,./<>?":
        str2 = str2 + i
print(str2)


#Write a program to transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[j][i], end=" ")
    print()
    
