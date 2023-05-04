def max_sum(arr,k):
    j=len(arr)-2
    i=len(arr)-1
    arr.sort()
    sum=0
    n_lis=[]
    while(i>0):
        if abs(arr[i]-arr[j])<k:
            sum=sum+arr[i]+arr[j]
            n_lis.append((arr[j],arr[i]))
            if j-2>=0 : 
                i=j-1
                j=j-2
            else: 
                break    
        else:
            if j-1>=0:
                i=i-1
                j=j-1
            else:
                break  
      
    print("sum %d"%sum)
    print(n_lis)
lis=[5,10,15,300]
k=12
max_sum(lis,k)                        