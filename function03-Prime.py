def prime(num):
    count =0
    for i in range (1,num+1):
        if num%i ==0:
            count+= 1

    if count ==2:
        print(f"The number {num} is prime")
    else:
        print(f"The number {num} is not a prime")
    return count
num = int(input("Enter the nuber : "))
prime(num)