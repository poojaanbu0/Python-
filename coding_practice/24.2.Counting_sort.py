def Counting_sort(arr): #time complex: O(n + k) , n = count elements, k = count-array size
# counts the occurences of the elements in the array 
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    
    count = [0] * (max+1)

    for num in arr:
        count[num] += 1

    result = []

    for num in range(len(count)):

        while count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result

arr = list(map(int, input("enter arr ").split()))
print(Counting_sort(arr))