

def bin_search(lis,l,u,n):
    while(l<=u):
     mid=(l+u)//2
     if lis[mid]==n:
        return mid
     if n<lis[mid]:
        u=mid-1
     if n>lis[mid]:
        l=mid+1        


lis=[2,3,4,5,6,7]
l=0
u=len(lis)-1
n=int(input("enter number to searched"))
pos=bin_search(lis,l,u,n)
if pos > -1:
    print("number found at ",pos+1)
else:
    print("not found")