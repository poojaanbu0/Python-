def intersection(a, b):
    res = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and a[i] not in res:
                res.append(a[i])
    return res

a = list(map(int, input("enter value ").split()))
b = list(map(int, input("enter value ").split()))
print(intersection(a,b))

