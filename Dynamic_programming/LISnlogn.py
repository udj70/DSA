def binarysearch(arr,low,upr,data):
    
    mid=low+(upr-low)//2
    if arr[mid]<=data and arr[mid+1]>=data:
        return mid+1
    else:
        if arr[mid]<data:
            return binarysearch(arr,mid+1,upr,data)
        else:
            return binarysearch(arr,low,mid-1,data)    
'''def LISnlogn(arr):
    I=[float('-inf')]
    L=[0 for _ in range(len(arr))]
    j=0
    for i in range(len(arr)+1):
'''
def linearsearch(arr,data):
    j=len(arr)-1
    while(arr[j]>=data):
        j-=1
    return j+1    
def LISnlogn(arr):
    I=[float('-inf')]
    L=[0 for _ in range(len(arr))]
    j=0
    for i in range(len(arr)):
        pos=linearsearch(I,arr[i])
        if pos>len(I)-1:
            I.append(arr[i])

        else:
            I=I[:(pos+1)]
            I[pos]=arr[i]
        L[i]=pos    
    return max(L)            

arr=[10,22,9,33,21,50,41,60,80]
print(LISnlogn(arr))

'''inf = 200000000
def get_lis_nlogn(arr):
    I = [inf] * len(arr)
    I[0] = -inf
    lis_len = 0
    for i in range(len(arr)):
        low, high = 0, len(arr)
        while (low <= high):
            mid = (low + high) / 2
            if I[mid] < arr[i]:
                low += 1
            else:
                high = mid - 1
        I[low] = arr[i]
        if lis_len < low:
            lis_len = low
    return lis_len
        

get_lis_nlogn([50, 3, 10, 7, 80, 40])
'''






