def  bubble(elements):
    size= len(elements)
    for i in range (size- 1):
        for j in range (size-1):
            if elements[j]>elements[j+1]:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
    return elements

a= int(input("Enter the number of elements:  "))
mylist=[]
print ("Enter the element:  ")
for i in range(a):
    b=int(input())
    mylist.append(b)

print ("The sorted list is: ", bubble(mylist))