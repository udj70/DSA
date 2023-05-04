def logestSubstring(s,k):
    start=0
    end=0
    m=1
    characters={}
    while(end<len(s)):
        if s[end] in characters :
            characters.pop(s[start])
            start+=1
        else:
            characters[s[end]]=1
            m=max(end-start+1,m)
            end+=1    
    return m 
s='abcdefab'
print(logestSubstring(s,7))



