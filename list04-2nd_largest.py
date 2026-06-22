# Find the second greatest element
arr = list(map(int,input("Enter the elements : ").split()))
largest = arr[0]
sec_largest = -1
index = arr[0]
for i in range(len(arr)):
    if arr[i]> largest :
        sec_largest = largest 
        index  = i
        largest = arr[i]
    elif arr[i] > sec_largest and arr[i]!= sec_largest:
        sec_largest = arr[i]

print(f"The second largest element is : {sec_largest} and index is {index}")