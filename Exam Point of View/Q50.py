# Python program to change Numbers into Words
a=int(input("Enter a number: "))
b={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
while a>0:
    print (b[a%10])
    a=a//10