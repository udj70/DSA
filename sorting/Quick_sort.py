import time
count=0
def partition(lis,lower,upper):
    global count
    pivot=upper
    j=lower-1
    count+=upper-lower-1
    for k in range(lower,pivot):

        if lis[k]<lis[pivot]:
            temp=lis[j+1]
            lis[j+1]=lis[k]
            lis[k]=temp
            j+=1

    temp=lis[j+1]
    lis[j+1]=lis[pivot]
    lis[pivot]=temp
    return j+1
def Quicksort(lis,lower,upper):
    global count
    if lower<upper:
        pivot=partition(lis,lower,upper)
        Quicksort(lis,lower,pivot-1)
        Quicksort(lis,pivot+1,upper)
    return lis  
start_time=time.time()
lis=[2,3,8,5,7,3,4,6]
new_lis=Quicksort(lis,0,len(lis)-1)
print(new_lis)
print(time.time()-start_time) #execution time 0.0009431838989257812



#simple and clear code
def partition(arr,m,n):
    pivot=arr[n]
    i=m-1
    j=m
    while(j<n):
        if arr[j]<=pivot:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        j+=1
    temp=arr[i+1]
    arr[i+1]=arr[n]
    arr[n]=temp
    return i+1        
    
def quicksort(arr,i,j):
    if i<=j:
        k=partition(arr,i,j)
        quicksort(arr,i,k-1)
        quicksort(arr,k+1,j)
    else:
        return    

arr=[5,4,3,2,1]#[3,2,5,6,3,4]
quicksort(arr,0,4)
print(arr)




