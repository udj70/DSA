'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

approach- bottom up dp- start comparing last chars in both string, if last chars matches or last char in pattern is . then no decision required.dp[i][j]= dp[i-1][j-1]
                        if last two chars not matchs, pattern have * at last now, so compare with char before * in pattern, and there will be three decision in decisions tree,
                        1. consider current regex for current char if same
                        2. if only one char in string present corresponding to regex, then also consider it and dp[i][j]=dp[i-2][j-1]
                        3. dont consider current regex for current char, we assume that some more regex may be present in previous positions for current char, so dp[i][j]= dp[i-2][j]
                        if charcter befind * does not macth with current char, simply ignore current regex then, dp[i][j]=dp[i-2][j]
    
refer this problem discussion panel on leetcode
'''
def isMatch(s: str, p: str) -> bool:
        dp=[[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]

        #if nor pattern and no regex then it is valid pattern match
        dp[0][0]=True

        # if string is empty but some regex is there, it can be true based on below condition
        for i in range(1,len(p)+1):
            if p[i-1]=="*" and dp[i-2][0]:
                dp[i][0]=True
        
        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                # if either last char matches or pattern have . so it is valid match, check in previous characters in string and pattern both
                if s[j-1]==p[i-1] or p[i-1]==".":
                    dp[i][j]=dp[i-1][j-1]
                # if not match then check if * is present at last
                elif p[i-1]=="*":
                    # if * present then check if previous char is same as current cahr in string, or it is .
                    # then 3 scenarios will be considered
                    if s[j-1]==p[i-2] or p[i-2]==".":
                        dp[i][j]=dp[i][j-1] or dp[i-2][j-1] or dp[i-2][j]
                    # simply ignore current regex, and check previous regex chars
                    else:
                        dp[i][j]=dp[i-2][j]
        print(dp)
        return dp[len(p)][len(s)]
string="aa"
pattern=".*" #here . is one character from a-z and * represent 0 or any repetition of char in range a-z
print(isMatch(string,pattern))