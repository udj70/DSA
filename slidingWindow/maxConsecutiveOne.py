#given 0,1 array
#replace k zeros at max to get max range of consecutive ones


def maxConsecutiveOne(arr,k):
    i=0
    j=0
    zero=0
    m=0
    while(i<=j and j<len(arr)):
        if arr[j]==0:
            if zero+1<=k:
                m=max(m,j-i+1)
                zero+=1
                j+=1
            else:
                if arr[i]==0:
                    zero=zero-1
                    
                
                i+=1            
        else:
            m=max(m,j-i+1)
            j+=1        
    return m
arr=[0,0,1,0,0,0,0,1,1,1,0,0,0,1]
print(maxConsecutiveOne(arr,3))                