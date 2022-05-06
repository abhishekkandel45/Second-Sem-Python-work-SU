# Python program to change Numbers into Words
a=(input("Enter a number: "))
b={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
#Seprate the number into a list
a=list(a)
#Create a new list
c=[]
#Loop through the list
for i in a:
    #Change the number into words
    c.append(b[int(i)])
#Print the list
print (c)
#Print the words
print (" ".join(c))
