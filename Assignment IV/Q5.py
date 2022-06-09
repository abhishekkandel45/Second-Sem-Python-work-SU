#Q5. Write program to read and write files in python?
f_name=input("Enter the name of the file: ")
#File should be in the same directory as the python file
f=open(f_name,"w")
f.write("Hello World")
f.close()
f=open(f_name,"r")
print(f.read())
f.close()
