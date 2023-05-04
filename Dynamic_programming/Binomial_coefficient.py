#calculate 
#Tc=O(n*r)
#Sc=O(r)
def ncr(n,r):
    c=[0]*(r+1)
    c[0]=1
    for i in range(1,n+1):
        j=min(i,r)
        while(j>0):
            c[j]=c[j]+c[j-1]
            j-=1
    return c[r]
print(ncr(5,0))            
