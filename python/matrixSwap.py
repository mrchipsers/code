def swapMatrix(matrix: list[list]):
    for y in range(len(matrix)):
        for x in range(y+1, len(matrix[y])):
            matrix[y][x], matrix[x][y]=matrix[x][y], matrix[y][x]
    return matrix

print(swapMatrix([[1,2,3],[4,5,6],[7,8,9]]))

def sortListList(lst: list):
    for i, val in enumerate(lst):
        lst[i]=sort(val)
    return lst

def sort(list):
    for i in range(len(list)):
        smallest_index=i
        for j in range(i,len(list)):
            if list[j]>list[smallest_index]:
                smallest_index=j
        list[i], list[smallest_index]= list[smallest_index],list[i]
    return list

print(sortListList([[1,3,2],[5,4,6],[9,8,7]]))