def birthday_cake_candles(arr):
    if(len(arr)<=0):
        return 0
    big=biggest(arr)
    index=0
    for num in arr:
        if(num==big):
            index+=1
    return index
        

def biggest(arr):
    sort(arr,0,len(arr)-1)
    return arr[len(arr)-1]

def sort(arr,first,last):
    if(len(arr)>1):
        index=partition(arr,first,last)
        if (first < index - 1):
            sort(arr,first,index-1)
        if (index < last):
            sort(arr,index,last)
            
def partition(items, left, right) :
    pivot= items[left]
    i= left
    j= right
    while (i <= j):
        while (items[i] < pivot):
            i+=1
        while (items[j] > pivot):
            j-=1
        if (i <= j):
            swap(items, i, j)
            i+=1
            j-=1
    return i

def swap(arr,first,last):
    temp=arr[first]
    arr[first]=arr[last]
    arr[last]=temp


print(birthday_cake_candles([3, 2, 1, 3]))