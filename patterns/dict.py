student = {
    "name": "Pooja",
    "age": 22,
    "marks": 95
}

text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0)+1

print(freq)

cache = {}

def square(n):
    if n in cache:
        return cache[n]

    cache[n] = n*n
    return cache[n]

students = [
("Math","John"),
("Math","Alice"),
("Physics","Bob")
]