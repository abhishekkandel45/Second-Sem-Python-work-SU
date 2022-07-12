#Write a program to define function dec_binary(num) to convert the existing decimal  number into its equivalent binary number

def dec_binary(num):
    if num>1:
        dec_binary(num//2)
    print(num%2,end="")

a=int(input("Enter the Decimal number: "))
dec_binary(a)