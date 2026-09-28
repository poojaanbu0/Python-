def matrix_addition(A, B):

    rows = len(A)
    cols = len(A[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]

    return result


A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

result = matrix_addition(A, B)

for row in result:
    print(row)