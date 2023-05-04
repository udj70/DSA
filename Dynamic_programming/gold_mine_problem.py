def max_gold_mine(arr):
    memo=[[0 for i in range(len(arr))] 
                        for j in range(len(arr))] 
    n=len(arr)-1
    for i in range(n+1):
        memo[i][n]=arr[i][n]   
    print(memo)    
            
    for j in range(n-1,-1,-1):
        for i in range(n+1):
            if i==0:
                memo[i][j]=arr[i][j]+max(memo[i][j+1],memo[i+1][j+1])
            else:
                if i==n:
                    memo[i][j]=arr[i][j]+max(memo[i][j+1],memo[i-1][j+1])
                else:
                    memo[i][j]=arr[i][j]+max(memo[i+1][j+1],memo[i][j+1],memo[i-1][j+1])
    print(max(m[0] for m in memo))            
arr=[[10,33,13,15],
      [22,21,4,1],
      [5,0,2,3],
      [0,6,1,2]]
max_gold_mine(arr)          