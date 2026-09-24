def quick_sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i
arr=[10,2,4,12]
quick_sort(arr,0,len(arr)-1)
print(arr)

#METHOD-2
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    right=[]
    for i in range(len(arr)-1):
        if arr[i]<=pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)
arr=[10,2,17,4]
print(quick_sort(arr))