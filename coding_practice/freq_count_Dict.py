# def frequency(a):
#     freq = {}

#     for num in a:
#         freq[num] = freq.get(num,0) + 1
#     print(freq)

# s = list(map(int, input("enter array").split()))
# frequency(s)

# s = ['1', '2', '3', '4']
# res = map(int, s)
# print(res)
# print(next(res))
# print(next(res))
# print(next(res))
# print(list(res))
# print(list(res))

arr = list(map(int, input("Enter array: ").split()))

for i in range(len(arr)):

    # Don't print the same number again
    already_counted = False

    for k in range(i):
        if arr[k] == arr[i]:
            already_counted = True
            break

    if already_counted:
        continue

    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    print(arr[i], "->", count)