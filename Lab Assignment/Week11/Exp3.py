#Write a program to compute the number of chracters, words and lines in a file.


#For Chracters:
a=open("exp1.txt","r")
b=a.read()
c=0
for i in b:
    c=c+1
print(c)
a.close()

#For finding numbers of words:
d=open("exp1.txt","r")
e=d.read()
f=1
for i in e:
    if i==" ":
        f=f+1
print(f)
d.close()

#For finding numbers of lines:
g=open("exp1.txt","r")
h=g.read()
j=1
for i in h:
    if i=="\n":
     j=j+1   
print(j)
g.close()

