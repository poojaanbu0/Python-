# def missing_number(arr):

#     arr.sort()

#     for i in range(len(arr)):
#         if arr[i] != i:
#             return i

#     return len(arr)

# arr = list(map(int, input("enter values ").split()))
# print(missing_number(arr))

def missing(arr):

    xor = 0

    for i in range(len(arr) + 1):
        xor = xor ^ i
        print("xor i", xor)

    for num in arr:
        xor = xor ^ num

    return xor

arr = list(map(int, input("enter values ").split()))
print(missing(arr))