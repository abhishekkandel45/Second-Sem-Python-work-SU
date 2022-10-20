# Name:  Roshan Bhatta              Date Assigned:    
# Course:  2000-Sec                 Date Due:           
# File name:                      
# Program Description: This is a program that will generate the password for the user as per the given criteria.

#taking the input from the user
words = input("Enter the words you want to use in your password: ")
#Initializing Count=0 for counting the number of words
count=0
#While loop for Prompting the user to enter the two words or more than two words if the user enters less than two words
while count<1:
    for i in words:
        if i==" ": 
            count+=1
    #if the number of spaces is less than 1 then the count will be 0 and the while loop will run again and again
    if count<1:
        count=0
        print("You must enter two or more words")
        words = input("Enter the words you want to use in your password: ")

# Using a for loop, create a password from the user’s input using the following scheme:
password = ""
for i in words:
    if i == " ":
        password += "?"
    elif i == "A" or i == "a":
        password += "0"
    elif i == "E" or i == "e":
        password += "1"
    elif i == "I" or i == "i":
        password += "2"
    elif i == "O" or i == "o":
        password += "3"
    elif i == "U" or i == "u":
        password += "4"
    elif i == "R" or i == "r":
        password += "*"
    elif i == "S" or i == "s":
        password += "@"
    elif i == "T" or i == "t":
        password += "&"
    else:
        password += i
# 4. Finally, display the password to the user
print("Your password is: ", password)