def minimum_swaps(arr):
    fLength=len(arr)
    i=0
    j=0
    while i<fLength:
        while j<fLength-i:
            if(s[j]!=s[i+j]):
                break
            j+=1
            counter+=1
        i+=1
        j=0

# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]