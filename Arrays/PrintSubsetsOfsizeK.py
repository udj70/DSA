def subset(arr,k,count,s,n,ans):
    #when count of elemnt in ans is k then print ans and return 
    if count==k:
        print(ans)
        return
    for i in range(s,n):
        #this condition is to check if consecutive elements are same, then include it only once
        if i!=s and arr[i]==arr[i-1]:
            continue
        #insert ith element, and call recusively from i+1 
        ans.append(arr[i])
        subset(arr,k,count+1,i+1,n,ans)
        #backtrack and remove the last inserted value
        ans.pop()    
A=[1,1,2,5,4,3]
ans=[]
subset(A,3,0,0,len(A),ans)