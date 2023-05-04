#Aplications of catalan numbers
#1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

#2) Count the number of possible Binary Search Trees with n keys, Cn (See this)

#3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.

#4) Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.(n points- Cn/2 chords)

#5) Number of ways a convex polygon of n+2 sides can split into triangles by connecting vertices.(for n vertices num of triangle = Cn-2 )

#6) Number of different Unlabeled Binary Trees can be there with n nodes. Cn

#7) The number of paths with 2n-2 steps on a rectangular grid from bottom left, i.e., (n-1, 0) to top right (0, n-1) that do not cross above the main diagonal.
#   (number of vertical movement should always greater then horizontal at any point of time)(for NxN grid num of ways= Cn), same as valleys and mointain

#8) Count number of valleys and mountains using  / \ in such a way that mountains should  be above ground level always(i.e number of / should always be greater
#    that \ at any moment of time)(for n pairs of upstox and downstokes possible valleys and mountain combination is Cn)

def nth_catalan_recursive(n):
    if n<=1:
        return 1
    res=0
    for i in range(n):
        res+=nth_catalan_recursive(i)*nth_catalan_recursive(n-i-1)    
    return res
#exponential time    
def nth_catalan_dp(n):
    if n==0 or n==1:
        return 1
    catalan=[0 for i in  range(n+1)]
    #initialize first two cataln numbers
    catalan[0]=1
    catalan[1]=1
    for i in range(2,n+1):
        for j in range(i):
            catalan[i]+=catalan[j]*catalan[i-j-1]
    return catalan[n]   
#o(n^2) time
def nth_catalan_binomial_coefficient(n):         
    #calculate 2*nCn//n+1=nth catalan number
    N=2*n
    K=n 
    res=1
    #we know that nCk=nCn-k
    if N-K<K:
        K=N-K
    # Calculate value of [n * (n-1) *---* (n-k + 1)] 
    # / [k * (k-1) *----* 1] 
    for i in range(K): 
        res = res * (N- i) 
        res = res //(i + 1) 
    return res//(n+1)
#o(n) time


print(nth_catalan_recursive(5))
print(nth_catalan_dp(5))
print(nth_catalan_binomial_coefficient(5))
