#calculate nPr
#formula->P(n,r)=P(n-1,r)+r*P(n-1,r-1)
#using dp->TC=O(n*r)
            #SC=O(n*r)
def permCoeff(n,r):
    P=[[0 for _ in range(r+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,r)+1):
            if j==0:
                P[i][j]=1
            else:
                P[i][j]=P[i-1][j]+ j*P[i-1][j-1]
            #if j<r:
             #   P[i][j+1]=0
    return P[n][r]
print(permCoeff(10,2))                

#can be better done by O(n) time using O(n) space
#P(n,r)=fact(n)//fact(n-r)
#simply calculate factorial till n
#return P[n][r]
