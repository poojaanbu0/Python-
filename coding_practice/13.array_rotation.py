#time complexity : O(k x n), k postitions , n elements

# def array_rot(arr,k,rotate):
#     k = k % len(arr)
#     if rotate == "right":
#         while k > 0:
#             x = len(arr)
#             last = arr[x-1]

#             for i in range(len(arr) - 1, 0, -1):
#                 arr[i] = arr[i-1]
#             arr[0] = last
           
#             k -= 1
#         print(arr)

#     if rotate == "left":
#         while k > 0:
#             x = len(arr)
#             first = arr[0]

#             for i in range(0, x-1):
#                 arr[i] = arr[i+1]
#             arr[x-1] = first
        
#             k -= 1
#         print(arr)


def array_rot(arr,k,rotate):
    if len(arr)== 0:
        return []
    #slicing
    k = k % len(arr)
    if rotate == "left":
      
        return arr[k:] + arr[:k]

    if rotate == "right":
        start = len(arr) - k
        
        return arr[start:] + arr[:start]

arr = list(map(int, input("enterr arr ").split()))
k = int(input("enter k "))
rotate = input("enter choice: 1.right 2.left ")
print(array_rot(arr, k, rotate))