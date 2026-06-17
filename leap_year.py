leap = int(input("Enter the year : "))
if(leap%400 ==0) or (leap%4 ==0 and leap%100 !=0):
    print("The year is leap year.")
else:
    print("Not a leap year.")