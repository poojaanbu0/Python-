def move_zeros(arr):
    j = 0

    # Step 1: Move all non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1

    # Step 2: Fill the remaining positions with zeros
    while j < len(arr):
        arr[j] = 0
        j += 1

    return arr


arr = list(map(int, input().split()))
print(move_zeros(arr))