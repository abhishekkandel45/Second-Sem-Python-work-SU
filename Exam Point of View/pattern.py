# Write a python program to create following pattern
#1
#1 2
#1 2 1
#1 2 1 2
#1 2 1 2 1
#1 2 1 2
#1 2 1
#1 2
#1
s=int(input("Enter the number of rows: "))
for i in range(s):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range(s):
    for j in range(s-i):
        print(j+1,end=" ")
    print()
