list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd=[]
even=[]
for i in range(len(list)):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])
print ("odd list is =", odd)      
print ("Even list is= ", even) 

mer=odd+even
print (mer)

#soerting the mer
sort_list = []
while mer:
    min = mer[0]  
    for a in mer:
        if a < min:
            min = a
    sort_list.append(min)
    mer.remove(min)
print (sort_list)