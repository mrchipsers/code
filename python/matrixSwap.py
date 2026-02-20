def swapMatrix(matrix: list[list]):
    for y in range(len(matrix)):
        for x in range(y+1, len(matrix[y])):
            matrix[y][x], matrix[x][y]=matrix[x][y], matrix[y][x]
    return matrix

print(swapMatrix([[1,2,3],[4,5,6],[7,8,9]]))