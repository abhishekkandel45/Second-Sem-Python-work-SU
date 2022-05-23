#Write a program that accepts sentences and build dictionary with LETTERS, DIGITS, UPPER CASE, LOWER CASE as key values and their count in the sentences as values.
#For example: Sentences=” Python-2022”
#d={“ LETTERS “:4, “DIGITS”:4,” UPPER CASE”:1,” LOWER CASE”:5}

string=input("Enter a string: ")
cletters=0
cdigits=0
cuppercase=0
clowercase=0
d={}
for i in string:
    if i.isalpha():
      cletters=cletters+1
    if i.isdigit():
      cdigits=cdigits+1
    if i.isupper():
      cuppercase=cuppercase+1
    if i.islower():
      clowercase=clowercase+1
d["LETTERS"]=cletters
d["DIGITS"]=cdigits
d["UPPER CASE"]=cuppercase
d["LOWER CASE"]=clowercase
print(d)
