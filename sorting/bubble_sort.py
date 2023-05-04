def sort(lis):
    for i in range(len(lis)-1): #for in in range(len(lis)-1,0,-1) #-1 means reverse order
        for j in range(len(lis)-i-1): # for j in range(i)
            if lis[j]>lis[j+1]:
                temp=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
lis=[5,4,6,3,5,8,6]
sort(lis)
print(lis)