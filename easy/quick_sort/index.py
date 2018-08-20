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

arr=[10,8,7,9,3,2,1,4,6,5,0]
sort(arr,0,len(arr)-1)
print(arr)