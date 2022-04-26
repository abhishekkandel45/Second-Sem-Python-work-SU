# Write a program to find the second larget number in a list without using any built-in function
size=int(input("Enter the size of list: "))
list=[]
for i in range(size):
    ele=int(input("Enter the element: "))
    list.append(ele)
print(list)
large=list[0]
second_large=list[0]
for i in range(size):
    if list[i]>large:
        second_large=large
        large=list[i]
print("The second largest number is: ",second_large)
