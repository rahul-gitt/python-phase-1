# Check if List is sorted or not.
arr = list(map(int, input("Enter the elements : ").split()))
sorted = True
for i in range(len(arr)-1):
    if arr[i]> arr[i+1]:
        sorted = False
        break

if(sorted):
    print("The list is sorted.")
else:
    print("The list is not sorted.")