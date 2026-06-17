sec = int(input("Enter total seconds : "))
hr = sec // 3600
min = (sec % 3600)// 60
second = sec % 60
print(f"Hours : {hr}")
print(f"Minutes : {min}")
print(f"Seconds : {second}")