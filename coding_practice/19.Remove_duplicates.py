def remove_duplicates(arr):
    result = []

    for i in range(len(arr)):
        duplicate = False

        for j in range(i):
            if arr[i] == arr[j]:
                duplicate = True
                break

        if duplicate == False:
            result.append(arr[i])

    return result

def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

arr = list(map(int, input("Enter array: ").split()))

print(remove_duplicates(arr))

##remove duplicates from string