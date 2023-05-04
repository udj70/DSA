def merge(list1,list2):
    i=0
    j=0
    l=len(list1)
    m=len(list2)
    ans=[0]*(m+l)
    c=0
    while(i<l and j<m):
        if list1[i]<=list2[j]:
            ans[c]=list1[i]
            c+=1
            i+=1
        else:
            ans[c]=list2[j]
            c+=1
            j+=1
    while(i<l):
        ans[c]=list1[i]
        i+=1
        c+=1
    while(j<m):
        ans[c]=list2[j]
        j+=1
        c+=1
    return ans    




def mergesort(arr,i,j):
    if i==j:
        return arr[i:j+1]
    if i<j:
        mid=i+(j-i)//2
        left=mergesort(arr,i,mid)
        right=mergesort(arr,mid+1,j)
        a=merge(left,right)
    return a    
      
    
arr=[5,4,3,2,1]
print(mergesort(arr,0,len(arr)-1))
#print(merge(arr,arr1))