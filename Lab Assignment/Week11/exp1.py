# Write a program to read and write from a file.
a=open("exp1.txt","w")
a.write(input("Enter the text: "))
a.close()
b= open("exp1.txt","r")
print(b.read())
b.close()