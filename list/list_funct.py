# # # numbers = [10, 20, 30]

# # # numbers.append(40)

# # # print(numbers) # orignal list modified

# # # numbers = [10, 20]

# # # numbers.extend([30, 40, 50])

# # # print(numbers) # orignal list modified

# # # fruits = ["apple", "banana"]

# # # fruits.insert(1, "orange")  # (index, object)

# # # print(fruits) # orignal list modified

# # # numbers = [10, 20, 30]

# # # x = numbers.pop(2) # returns the removed element and an index can be specified to be removed

# # # print(x)
# # # print(numbers)# orignal list modified

# # # numbers = [10, 20, 30, 20]
# # # numbers.remove(20)
# # # print(numbers) # orignal list modified

# # # numbers = [1, 2, 3]

# # # numbers.clear()

# # # print(numbers) # orignal list modified

# # # numbers = [10, 20, 30]

# # # print(numbers.index(20)) # no list modified

# # # numbers = [10, 20, 20, 30]

# # # print(numbers.count(20)) # no list modified

# # # numbers = [5, 2, 8, 1]

# # # numbers.sort()

# # # print(numbers) #original list modified

# # # numbers = [1, 2, 3]

# # # numbers.reverse()

# # # print(numbers) #original list modified

# # # numbers = [1, 2, 3]

# # # new_list = numbers.copy()

# # # print(numbers)
# # # print(new_list)#new list created

# # # #list operations 
# # # a = [1, 2]
# # # b = [3, 4]

# # # c = a + b

# # # print(c) # new list created

# # # a = [1, 2]

# # # b = a * 3

# # # print(b) # new list created

# # # numbers = [10, 20, 30, 40]

# # # new = numbers[1:3]

# # # print(new) # new list created

# a = [1,2,3]

# b = a

# c = a.copy()
# a.append(4)
# print(id(a)==id(c))
# print(id(a)==id(b))

# a = [1,2]
# b = a * 3
# print(a)
# print(b)
# print(id(a)==id(b))
# a = [[1]]
# b = a * 3
# print(a)
# print(id(a)==id(b))
# b[0][0] = 100
# print(id(a)==id(b))
# print(a)
# print(id(a)==id(b))
# print(b)
a = []
a.append(3)
print(a)
# # a = [[1],[2]]

# # b = a[:]

# # b[0].append(5)

# # print(a)

# a = [[1],[2]]

# b = a[:]

# b[0].append(5)

# print(a)

# a = [1,2,34]
# n = len(a) -1 
# print(a[n:0:-1])
# a = [[1],[2]]
# b = a[:]
# b[0].append(5)
# print(a)
# print(id(a)==id(b))
# print(b)

# a = [1,2]

# b = a * 3
# print(id(a)==id(b))
# print(b)
# a=[1,2]

# a.insert(1,[210,20])

# print(a)
a = [0]*3
print(a)
a = [[0,0,0]]*3
print(a)

a = [[]]*2
a[0].append(2)
print(a)