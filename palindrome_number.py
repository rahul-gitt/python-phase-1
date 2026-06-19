num = int(input("Enter your number : "))
original = num
reverse = 0
while num>0 :
    last_digit = num %10
    reverse = reverse*10 + last_digit
    num = num//10
if(original == reverse):
    print("The number is Palindrome Number : ",reverse)
else:
    print("Not a palindrome number : ",reverse)