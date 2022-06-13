# Write a python program to write the content “Python programming” for the existing file?
f_name=input("Enter the name of the file: ")
f=open(f_name,"w")
f.write("Python programming")
f.close()
f=open(f_name,"r")
print(f.read())
f.close() 