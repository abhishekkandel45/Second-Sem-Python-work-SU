#A four digit integer is entered through keyboard. Write a function to calculate the sum of the four digit number without recursion and using recursion.

# Without recursion
def sum_without_recursion(num):
    sum=0
    while num>0:
        sum=sum+num%10
        num=num//10
    return sum

# With recursion
def sum_with_recursion(num):
    if num==0:
        return 0
    else:
        return num%10+sum_with_recursion(num//10)


        