def allParenthesis(curr,open_,close,N):
    global ans
    if  close==N:
        ans.append(curr)
        return
    if open_>close:
        allParenthesis(curr+")",open_,close+1,N)
    if open_<N:
        allParenthesis(curr+"(",open_+1,close,N)
    return 
ans=[]
allParenthesis("",0,0,3)
print(ans)