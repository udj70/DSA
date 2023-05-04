def find_next_just_largest(i,A):
    ans=-1
    temp=A[i]
    i+=1
    index=0
    while(i<len(A)):
        if A[i]>temp:
            if ans==-1:
                ans=A[i]
                index=i
            else:
                if A[i]<ans:
                    ans=A[i]
                    index=i
        i+=1
    return index                    


def next_p(A):
    #traverse form last check for condition A[i]<A[i+1],
    #if whole array is sorted in decreasing order then return sorted form of array
    found=False
    i=len(A)-2
    while(i>=0):
        if A[i]<A[i+1]:
            found=True
            break
        i-=1
    if not found:
        return A.sort()
    #if found then after i we have to find an element in A[i+1:] which is smallest 
    #among all larger elements(or just larger element) than A[i] and return its index    
    else:
        index=find_next_just_largest(i,A)
        #swap both
        A[i],A[index]=A[index],A[i]
        #after swaping A[i+1:] will sorted in decreasing order, 
        #so to achieve next larger permutation just reverse it i.e ascending order
        A[i+1:]=A[i+1:][::-1]
    return A
A=[1,2,5,4,3]
print(next_p(A))        



