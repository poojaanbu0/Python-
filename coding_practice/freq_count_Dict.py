a = [1,2,3,3,2,3,24,4]

freq = {}

for num in a:
    freq[num] = freq.get(num,0) + 1
print(freq)