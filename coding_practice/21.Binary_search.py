def binary_search(arr, n):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == n:
            return mid

        elif arr[mid] < n:
            low = mid + 1

        else: 
            high = mid - 1

    return -1

arr = list(map(int, input("enter the arr ").split()))
n = int(input("enter the value "))

res = binary_search(arr, n)

if res != -1:
    print("found at index", res)
else:
    print("not found")