
# Everything in python is a object ////////

# magic methods __init__, repr , eq
# @dataclass
# async
# Concurrency

# GIL global interface lock
# threads

class A:
    def __init__(self):
        print("Initializing A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Initializing D")

d = D()