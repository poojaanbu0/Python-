nums = [1, 2, 3, 2, 4, 5, 1]

unique = list(set(nums))

print(unique)

math = {"Alice", "Bob", "John"}
science = {"John", "Alice", "David"}

print(math & science)

blocked = {"spam", "fake", "bot"}

user = "fake"

if user in blocked:
    print("Blocked")

visitors = set()

visitors.add("Alice")
visitors.add("Bob")
visitors.add("Alice")

print(visitors)

dictionary = {"apple", "banana", "orange"}

word = "banana"

print(word in dictionary)

visited = set()

visited.add(5)

if 5 in visited:
    print("Already visited")