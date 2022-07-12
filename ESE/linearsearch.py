def search(list1, ele):
    for i in range(len(list1)):
        if ele==list1[i]:
            return ('Element Found at Index:',i)
            break
    else:
        return ("Element Not found")

a= int(input("Enter the number of Elements:  "))
list2=[]
print ("Enter the Element: ")
for i in range (1,a+1):
    b=int(input())
    list2.append(b)
print (list2)
c= int(input("Enter the element to Search: "))
print (search(list2,c))
