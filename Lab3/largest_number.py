# write a program to find the largest number in a list without using max() function
size=int(input("Enter the size of list: "))
list=[]
for i in range(size):
    ele=int(input("Enter the element: "))
    list.append(ele)
print(list)
large=list[0]
for i in range(size):
    if list[i]>large:
        large=list[i]
print("The largest number is: ",large)
