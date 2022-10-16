# Name:  Roshan Bhatta              Date Assigned:    
# Course:  2000-Sec                 Date Due:           
# File name:                      
# Program Description: This is a program that will generate the password for the user as per the given criteria.

# 1. Ask the user to enter
words = input("Enter 2 or more words: ")
# 2. If they don’t enter at least 2 words, Condition is Checked using Space as a delimiter
if len(words.split()) < 2:
    print("Error: You did not enter 2 or more words!")
    words = input("Enter 2 or more words: ")
# 3. Using a for loop, create a password from the user’s input using the following scheme:
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


