
# =====================================================
# Problem : Nested Tuple
# =====================================================


students = (
    ("Ram",85),
    ("John",91),
    ("Asha",78)
)

for name, marks in students:
    print(name, marks)


# =====================================================
# Problem : Tuple Packing and Unpacking
# =====================================================

student = ("Pooja",22,"Python")

name, age, course = student

print(name)
print(age)
print(course)


# =====================================================
# Problem : Find Duplicate Elements
# =====================================================

t = (1,2,3,4,2,5,1,6,3)

duplicates = set()

for num in t:

    if t.count(num) > 1:
        duplicates.add(num)

print(tuple(duplicates))


# =====================================================
# Problem : Remove Duplicates
# =====================================================



t = (1,2,3,2,4,1,5,3)

result = tuple(set(t))

print(result)


# =====================================================
# Problem : Second Largest Number
# =====================================================

t = (45,22,87,99,13,76)

unique = sorted(set(t))

print("Second Largest =", unique[-2])


# =====================================================
# Problem : Student Database
# =====================================================



students = (
    (101,"Ram",85),
    (102,"John",96),
    (103,"Asha",78),
    (104,"Rita",91)
)

total = 0

topper = students[0]

for student in students:

    print(student)

    total += student[2]

    if student[2] > topper[2]:
        topper = student

print("\nTopper:")
print(topper)

print("\nAverage:")
print(total / len(students))