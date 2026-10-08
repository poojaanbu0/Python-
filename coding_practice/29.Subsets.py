def subsets(arr, index, current):
    if index == len(arr):
        if current: # if you want to skip the empty element
            print(current)
        return 

    current.append(arr[index])
    subsets(arr, index + 1, current)

    current.pop()

    subsets(arr, index + 1, current)

arr = list(map(int, input("enter the arr ").split(",")))
subsets(arr, 0, [])