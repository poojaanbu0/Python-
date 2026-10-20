# def transpose(matrix):

#     rows = len(matrix)
#     cols = len(matrix[0])

#     result = [[0 for _ in range(rows)] for _ in range(cols)]

#     for i in range(rows):
#         for j in range(cols):
#             result[j][i] = matrix[i][j]

#     return result

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# result = transpose(matrix)

# for row in result:
#     print(row)

#how to get input for this for a matrix

def diagonal_sum(matrix):
    total = 0
    
    for i in range(len(matrix)):
        total += matrix[i][i]

    return total

rows, cols = map(int, input().split())
matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

print(diagonal_sum(matrix))
