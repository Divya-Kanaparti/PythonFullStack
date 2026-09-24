def merge_sort(arr):
    #BASE CONDITION
    if len(arr)<=1:
        return arr
    #MORE THAN 1 ELEMENT
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #ADD REMAINING ELEMENTS
    while i<len(left):
        result.append(left[i])
        i+=1
    #ADD REMAINING VALUES FROM RIGHT
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
arr=[4,2,3,1]
print(merge_sort(arr))