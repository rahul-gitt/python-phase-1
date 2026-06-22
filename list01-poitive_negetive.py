# Print positive and negative elements of an List
arr = list(map(int,input("Enter the elements : ").split()))
print("Positive numbers are :")
for i in arr:
    if i>=0:
        print(i)
print("Negative numbers are : ")
for i in arr:
    if i<0:
        print(i)