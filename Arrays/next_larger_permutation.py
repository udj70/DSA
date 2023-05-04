#same implementation of next larger number 
def next_permutation(num):
    i=len(num)-2
    found=False
    while(i>=0):
        if num[i]<num[i+1]:
            found=True
            break
        i-=1
    if not found:
            return num.sort()
    else:    
            max_index=findmax(i+1,num,num[i])
            num[i],num[max_index]=num[max_index],num[i]
            n2=num[i+1:]
            n2.sort()
            n1=num[:i+1]
            return n1+n2
def findmax(index,num,temp):
    ans=0
    idx=-1
    for i in range(index,len(num)):
        if num[i]>temp:
            if num[i]<ans:
                idx=i
                ans=num[i]

    return idx        


num=[1,2,3]
print(next_permutation(num))