import time
start_time=time.time()
lis=[2,3,4,5,4,3,4,5]
for i in range(1,len(lis)):
    j=i
    while(lis[j]<=lis[j-1] and j>0):
        temp=lis[j-1]
        lis[j-1]=lis[j]
        lis[j]=temp
        j-=1
print(lis) 
print(time.time()-start_time)       #time taken to execute 0.001195669174194336s