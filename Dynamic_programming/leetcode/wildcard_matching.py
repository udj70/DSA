'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

'''

# approach 1 - recursive

def solve_recursion(p,s,i,j):

    #base condition

    if i==0 and j>0:
        return False
    if j==0 and i>=0:
        for ii in range(0,i):
            if p[ii]!='*':
                return False
        return True
    
    # hypothesis and induction
    if p[i-1] == s[j-1] or p[i-1] =='?':
        return solve_recursion(p,s,i-1,j-1)
    if p[i-1]=='*':
        return solve_recursion(p,s,i,j-1)  or solve_recursion(p,s,i-1,j)
p='a?'
s='aa'
print("recursion",solve_recursion(p,s,len(p),len(s)))

# approach 2- memoisation

def solve_memo(p,s,i,j,dp):

    #base condition

    if i==0 and j>0:
        return False
    if j==0 and i>=0:
        for ii in range(0,i):
            if p[ii]!='*':
                return False
        return True
    if dp[i][j]!=-1:
        return dp[i][j]
    
    
    # hypothesis and induction
    if p[i-1] == s[j-1] or p[i-1] =='?':
        dp[i][j] = solve_memo(p,s,i-1,j-1,dp)
    elif p[i-1]=='*':
        dp[i][j] = solve_memo(p,s,i,j-1,dp)  or solve_memo(p,s,i-1,j,dp)
    return dp[i][j]

p='a?'
s='aa'
dp=[[-1 for _ in range(len(s)+1)] for _ in range(len(p)+1)]
print("memoisation-",solve_memo(p,s,len(p),len(s),dp))

# approach 3- tabulation
def solve_tab(p,s):
    dp=[[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
    for i in range(len(p)+1):
        for ii in range(0,i):
            if p[ii]!='*':
                dp[i][0] = False
        dp[i][0] = True
    for i in range(1,len(p)+1):
        for j in range(1,len(s)+1):
            if p[i-1] == s[j-1] or p[i-1] =='?':
                dp[i][j] = dp[i-1][j-1]
            elif p[i-1]=='*':
                dp[i][j] = dp[i][j-1]  or dp[i-1][j]
    return dp[i][j]

p='a*'
s='aa'
print("tabulation",solve_tab(p,s))

# approach 4- space optimised

def solve_opt(p,s):
    prev=[False for _ in range(len(s)+1)]
    curr=[False for _ in range(len(s)+1)]
    prev[0]=True
        
    for i in range(1,len(p)+1):
        for ii in range(0,i):
            if p[ii]!='*':
                curr[0] = False
        curr[0] = True
        for j in range(1,len(s)+1):
            if p[i-1] == s[j-1] or p[i-1] =='?':
                curr[j] = prev[j-1]
            elif p[i-1]=='*':
                curr[j] = curr[j-1]  or prev[j]
        prev=curr[:]
    return prev[j]
p='a*'
s='aa'
print("tabulation+ Space opt-",solve_opt(p,s))

