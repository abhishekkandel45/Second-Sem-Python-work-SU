# Write a program to find those numbers which are divisible by 5 and 7, between 1500 and 2700(Both included)
for i  in range (1500, 2701):
    if i%5==0 and i %7==0:
        print (i, end=" ")
