def quick_sort(arr): # average-case : o(n log n) worst-case: O(n^2)

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = []
    midd = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == arr[pivot]:
            midd.append(num)
        else:
            right.append(num)

    return quick_sort(left) + midd + quick_sort(right)

arr = list(map(int, input("enter arr ").split()))
quick_sort(arr)