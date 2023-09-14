print("Matrix Multiplication 2D")
matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# for i in matrix:
#     for j in i:
#         for k in j:
#             print(k, end=" ")

#         print()

#     print()

i = 0
multipliedMatrix = []
while i < len(matrix[0][0]):
    tempMultipliedMatrix = []

    j = 0
    while j < len(matrix[1]):
        tempMultipliedMatrix.append(
            matrix[0][i][0] * matrix[1][0][j] + matrix[0][i][1] * matrix[1][1][j]
        )

        j += 1

    multipliedMatrix.append(tempMultipliedMatrix)

    i += 1

for i in multipliedMatrix:
    print(i)
