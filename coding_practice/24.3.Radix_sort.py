def radix_sort(arr): # O(d(n + k))

    if len(arr) <= 1:
        return arr

    maxi = max(arr)

    exp = 1

    while maxi // exp > 0:
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // exp ) % 10
            buckets[digit].append(num)

        arr = []

        for bucket in buckets:
            arr.extend(bucket)

        exp *= 10

    return arr

arr = list(map(int, input("enter arr ").split()))
print(radix_sort(arr))