# Bubble Sort
def bubblesort(list):
    for n in range(len(list)-1,0,-1):
        for i in range(n):
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
list=[5,8,23,8,34,2,1,0]
bubblesort(list)
print(list)