
def diagonal_difference(arr):
    j=len(arr)-1
    leftToright=0
    rightToLeft=0
    for i in range(len(arr)):
        leftToright=leftToright+arr[i][i]
        rightToLeft=rightToLeft+arr[i][j]
        j=j-1
    result=leftToright-rightToLeft
    return -1*result if result<0 else result

print(diagonal_difference([[1, 2, 3],[4, 5, 6],[9, 8, 9]]))