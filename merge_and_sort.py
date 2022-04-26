# Write a program that creat 2 list and merge them and sort them in ascending without using any function
size=int(input("Enter the size of list: "))
list1=[]
list2=[]
for i in range(size):
    ele=int(input("Enter the element: "))
    list1.append(ele)
for i in range(size):
    ele=int(input("Enter the element: "))
    list2.append(ele)
list3=list1+list2
sort_list = []
while list3:
    min = list3[0]  
    for x in list3: 
        if x < min:
            min = x
    sort_list.append(min)
    list3.remove(min)    
print("The sorted list is: ",sort_list)