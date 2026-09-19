a = 3
print(id(a))
x = id(a)
a = 2
y  = id(a)
print(x == y)

mixed_tuple = (1, [2, 3])
# mixed_tuple[0] = 5  # Fails! Tuple structure is locked.

mixed_tuple[1].insert(1,4) 
print(mixed_tuple)     # Works! Output: (1, [2, 3, 4])


#PASS-BY-ASSIGNMENT
def modify_immutable(x):
    x += 10  # Creates a NEW integer object; rebinds local 'x'
    print(f"Inside function: {x}")

num = 5
modify_immutable(num)
print(f"Outside function: {num}")  # Output: 5 (Unchanged)

# The Correct Way: Use None as an immutable sentinel value
def append_to_list(element, target_list=None):
    if target_list is None:
        target_list = []  # A brand new list is created at call time
    target_list.append(element)
    return target_list

# Every call now works independently
print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2]

from typing import Optional

# Python 3.10+ syntax
def process_data(data: dict | None = None) -> dict:
    if data is None:
        data = {}
    return data

# Pre-Python 3.10 syntax
def process_data_older(data: Optional[dict] = None) -> dict:
    if data is None:
        data = {}
    return data

#python dataclasses use the field(default_factory= list)

# 1. Initialize from a string (requires an explicit encoding)
ba = bytearray("Hello", "utf-8")

# 2. Modify an element using its index (assigning an integer value 0-255)
ba[0] = 66  # 66 is the ASCII code for 'B'
print(ba)  # Output: bytearray(b'Bello')

# 3. Append a new byte to the end
ba.append(33)  # 33 is the ASCII code for '!'
print(ba)  # Output: bytearray(b'Bello!')

# 4. Use list-like methods like extend or slice assignment
ba.extend([10, 11])
print(ba)
