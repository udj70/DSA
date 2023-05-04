def pascal(n):
    arr=[[0 for i in range(n)] for j in range(n)]
    arr[0][0]=1
    for i in range(len(arr)):
        arr[i][0]=1
        for j in range(1,i+1):
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
    return arr        
n=int(input())
arr=pascal(n)
for a in range(len(arr)):
    print(" "*(n-a),end='')
    print(" ".join(map(str,arr[a][:a+1])))
