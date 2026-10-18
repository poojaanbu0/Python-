# def remove_duplicates(arr):
#     result = []

#     for i in range(len(arr)):
#         duplicate = False

#         for j in range(i):
#             if arr[i] == arr[j]:
#                 duplicate = True
#                 break

#         if duplicate == False:
#             result.append(arr[i])

#     return result

# def remove_duplicates(arr):
#     seen = set()
#     result = []

#     for num in arr:
#         if num not in seen:
#             result.append(num)
#             seen.add(num)

#     return result

# arr = list(map(int, input("Enter array: ").split()))

# print(remove_duplicates(arr))

##remove duplicates from string

# def duplicate(arr):
#     freq = {}

#     for i in range(len(arr)):
#         freq[arr[i]] = freq.get(arr[i], 0) + 1

#     # if len(set(freq.values())) == 1:
#     #     return False
#     # return True

#     for count in freq.values():
#         if count > 1:
#             return True
#     return False

# arr = list(map(int, input("enter input ").split()))
# print(duplicate(arr))

#common elements

# def common(a, b):
#     resu = []
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i] == b[j] and a[i] not in resu:
#                 resu.append(a[i])

#     return resu

# a = list(map(int, input("Enter array: ").split()))
# b = list(map(int, input("Enter array: ").split()))
# print(common(a, b))


