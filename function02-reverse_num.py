def reverse_num(num):
    reverse = 0

    while num>0:
        digit = num%10
        reverse =  reverse*10 + digit
        num = num//10

    return reverse
    
num = int(input("Enter the number : "))
print("The reverse number is - ",reverse_num(num))