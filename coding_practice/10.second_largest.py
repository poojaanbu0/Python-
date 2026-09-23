def second_largest(arr):
    largest = 0
    second_largest = 0

    for i in arr:
        if largest < i:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    print(second_largest)
            
arr = list(map(int, input("enter array ").split()))
second_largest(arr)