#Write a program to define function dec_binary(num) to convert the existing decimal  number into its equivalent binary number

def dec_binary(num):
    while num>0:
        rem=num%2
        num=num//2
        print(rem,end="")

        