import time 
start=time.time()
def minJumpsToAvoidTrap(arr):
    primes_till_ith_index=[0]*(len(arr)+1)
    prime=[True]*(len(arr)+1)
    prime[0]=False
    prime[1]=False
    i=2
    count=0
    while(i*i<len(arr)+1):
        if prime[i]:
            count+=1
            for j in range(i*i,len(arr)+1,i):
                if prime[j]:
                    prime[j]=False
        primes_till_ith_index[i]=count
        i+=1
    while(i<len(arr)+1):
        if prime[i]:
            count+=1
        
        primes_till_ith_index[i]=count
        i+=1    
    print(primes_till_ith_index)
    jumps=[float('inf')]*len(arr)
    jumps[0]=0
    for i in range(1,len(arr)):
        if arr[i]=='#':
            for j in range(0,i):
                if arr[j]=='#' and (j+1==i or j+2==i) :
                    jumps[i]=min(jumps[i],jumps[j]+1)
    return jumps[len(arr)-1]


arr=['#','*','#','#','#','#','*','#']
res=minJumpsToAvoidTrap(arr)    
if res==float('inf'):
    print("NO Path")
else:
    print(res)            
print(time.time()-start)




