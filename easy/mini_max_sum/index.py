def mini_mux_sum(arr):
	little= big= 0
	sort(arr,0,len(arr)-1)
	for i in range(0,len(arr)-1):
		little=little+arr[i]
		big=big+arr[len(arr)-1-i]

	print(str(little)+" "+str(big))

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
            
mini_mux_sum([3, 1, 2, 4, 5])