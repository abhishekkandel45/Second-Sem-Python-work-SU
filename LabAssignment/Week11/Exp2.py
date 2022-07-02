#Write a program to count the frequecy of characters in the given file. Can you use character frequency to tell wheather the given file is Python file,
# C File or a text file?
a= open("exp1.txt","r")
b=a.read()
c=0
for i in b:
    c=c+1
print(c)
a.close()

f= open("exp1.txt","r")
g=f.read()
if g.find("python")!=-1:
    print("Python file")
elif g.find("c")!=-1:
    print("C file")
else:
    print("Text file")
f.close()
