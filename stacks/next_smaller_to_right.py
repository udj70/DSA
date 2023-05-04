#note:-1. when smaller to right/left is asked always keep smallest elemnt on top of stack
#      2. smaller/larger to right -> traverse stack from right to left
#      3. smaller/larger to left -> traverse stack from left to right
def next_smaller_to_right(arr):
    ans=[-1]*len(arr)
    stack=[]
    j=len(arr)-1
    for a in arr[::-1]:
        while(len(stack) and stack[-1]>=a):
            stack.pop()
        if len(stack)==0:
            ans[j]=a    
        else:
            ans[j]=stack[-1]
        j-=1    
        stack.append(a)
    return ans

arr=[1,5,3,0,10,2]
ans=next_smaller_to_right(arr)
print(ans)