size= int(input("Enter the size of the list: "))
list=[]
for i in range (size):
    ele=int(input("Enter the element for the list: "))
    list.append(ele)
print (list)
large = list[0]
for i in range(len(list)):
    if list[i]>=large:
        large=list[i]
print (large)
