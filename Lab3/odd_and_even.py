# write a program to create a list that contains numbers and then find even and odd numbers in the list separately
size=int(input("Enter the size of list: "))
list=[]
for i in range(size):
    ele=int(input("Enter the element: "))
    list.append(ele)
print(list)
even=[]
odd=[]
for i in range(size):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])
print("The even numbers are: ",even)
print("The odd numbers are: ",odd)
