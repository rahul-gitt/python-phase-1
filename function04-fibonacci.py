def fibonacci(num):
    a= 0
    b=1
    for i in range(num):
        print(a,end = " ""\n")
        c = a+b
        a = b
        b = c
    return 
num = int(input("Enter the series number : "))
fibonacci(num)
