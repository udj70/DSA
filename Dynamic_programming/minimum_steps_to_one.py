def min_steps(n):
    if n<1:
        return 0
    if n==1:
        return 0
    return 1+min(min_steps(n/3),min_steps(n/2),min_steps(n-1))    


n=int(input())
print(min_steps(n))
