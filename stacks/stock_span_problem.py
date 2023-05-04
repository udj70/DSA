#task- find count of consecutive smaller element to left
#approach- use stack and save index of next larger to left and calculate difference fof curent index and that index
def consecutive_smaller_to_left(arr):
    ans=[]
    stack=[]
    for i in range(len(arr)):
        while(len(stack) and arr[i]>arr[stack[-1]]):
            stack.pop()
        if len(stack)==0:
            ans.append(1)
        else:        
            temp=i-stack[-1]
            ans.append(temp)
        stack.append(i)    
    return ans    

arr=[100,80,60,70,60,75,85]
print(consecutive_smaller_to_left(arr))