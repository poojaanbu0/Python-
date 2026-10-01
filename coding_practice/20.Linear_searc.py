def linear_search(arr, value):

    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

arr = list(map(int, input("enter value ").split()))
value = int(input())

res = linear_search(arr, value)

if res != -1:
    print("found at index", res)
else:
    print("not found")