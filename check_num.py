# check the number is divisible by both 3 & 5
num = int(input("Enter the number : "))
if(num%5==0 and num%3 ==0):
    print(f"The number is divisibe {num}")
else:
    print("Number not divisible")