def removeKdigits( num: str, k: int) -> str:
        stack=[-1]
        removed=0
        for n in num:
            while len(stack) and  int(n)<=stack[-1] and removed<k:
                stack.pop()
                removed+=1
            stack.append(int(n))
        while(removed<k):
            stack.pop()
            removed+=1
        ans=0
        m=1
        j=len(stack)-1
        print(stack)
        while(j>=1):
            ans+=m*stack[j]
            m*=10
            j-=1
        return ans
print(removeKdigits('123456',3))