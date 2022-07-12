#odd Range Fuinction
def odd_range(start, stop):
    for i in range(start, stop):
        if i % 2 != 0:
            print(i)

a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
odd_range(a,b)       