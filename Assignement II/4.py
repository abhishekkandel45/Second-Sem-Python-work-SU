#Q4. Write Python program to sort numbers in a list in ascending order using Merge Sort.
num=int(input("Enter the number of elements in the first list: "))
l1=[]
for i in range(num):
    l1.append(int(input("Enter the element: ")))
print("The first list is: ",l1) 
num2=int(input("Enter the number of elements in the second list: "))
l2=[]
for i in range(num2):
    l2.append(int(input("Enter the element: ")))
print("The second list is: ",l2)


#Defining ghr merge function
def merge(l1,l2):
    l3=[]
    while len(l1)>0 and len(l2)>0:
        if l1[0]<l2[0]:
            l3.append(l1[0])
            l1.remove(l1[0])
        else:
            l3.append(l2[0])
            l2.remove(l2[0])
    if len(l1)==0:
        l3=l3+l2
    else:
        l3=l3+l1
    return l3
def mergesort(l):
    if len(l)==1:
        return l
    mid=len(l)//2
    l1=mergesort(l[:mid])
    l2=mergesort(l[mid:])
    return merge(l1,l2)
print("The sorted list is: ",mergesort(l1+l2))