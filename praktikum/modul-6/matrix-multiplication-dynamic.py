matrixArray = [
    [[[1, 2]], [[3], [4]]],
    [[[1, 2]], [[3, 4], [5, 6]]],
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    [[[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]],
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12], [13, 14, 15]]],
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12], [13, 14, 15]]],
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]],
]


for matrixObject in matrixArray:
    i = 0
    matrixResultArray = []
    while i < len(matrixObject[0]):

        j = 0
        total = 0
        tempMatrixResultArray = [0 for _ in range(len(matrixObject[1][0]))]
        while j < len(matrixObject[1][0]):

            k = 0
            while k < len(matrixObject[0][i]):
                tempMatrixResultArray[j] += (
                    matrixObject[0][i][k] * matrixObject[1][k][j]
                )

                k += 1

            j += 1

        matrixResultArray.append(tempMatrixResultArray)

        i += 1

    for matrixResultObject in matrixResultArray:
        print(matrixResultObject)

    print()
