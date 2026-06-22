# Find the greatest element and print its index too
arr = list(map(int,input("Enter the elements : ").split()))
large = arr[0]
index = arr[0]
for i in range(len(arr)):
    if arr[i]>large:
        large = arr[i]
        index = i

print(f"Your lagest number is : {large} at index {index}")