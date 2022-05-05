# Write a pythin program to creat and access the elements in the array.
#create user defined array
a=[]
#create a loop to take input from user
for i in range(5):
    a.append(int(input("Enter the element: ")))
#print the array
print("The array is: ",a)
#create a loop to access the elements
for i in range(5):
    print("The element at index ",i," is: ",a[i])