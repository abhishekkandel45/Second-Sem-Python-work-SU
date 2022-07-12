def binary(mylist, target):
    left=0
    right= len(mylist)-1
    while left<=right:
        middle= (left+right)//2
        if target== mylist[middle]:
            return (" Element Found at index: ", middle)
            break
        elif target>mylist[middle]:
            left=middle+1
        else:
            right=middle-1
    return ("Element Not found on the list")



a= int(input("Enter the number of element you want to assign to the list: "))
list1=[]
for i in range (1, a+1):
    b=int(input("Enter the element: "))
    list1.append(b)

temp= list1
print ("unsorted list: ",list1)
temp.sort()
print ("Sorted List: ", temp)

c= int(input("Enter the Element to Search: "))
print (binary(temp,c))
