#task- Given- A string s, find a substring with all unique char.
#approach- use hasmap to store unique char, when substring length became equal to hash map, i.e all unique char present in cureent window, hence save ans



def longest_substring_with_all_unique_char(S):
    dic={}
    i=0
    j=0
    ans=0
    while(i<=j):
        if len(dic)<j-i:
            #i.e window size have some duplicates, so reduce window from left
            dic[S[i]]-=1
            if dic[S[i]]==0:
                dic.pop(S[i])
            i+=1
        elif len(dic)==j-i:
            #i.e no duplicates all unique
            ans=max(ans,j-i)

            #if j in not at last+1, then add it, else break loop
            if j<len(S):
                if S[j] in dic:
                    dic[S[j]]+=1
                else:
                    dic[S[j]]=1
                j+=1
            else:
                break
    return ans
def longest_substring_with_no_repeat_hash_approach(s):
        dic={}
        mx=0
        left=0
        right=0
        # intialize window left and right with 0, now increase window by incrementing right
        # if character at right is already present in dic, check its index, if it lies after left, increment left to dic[s[right]]+1 
        # or if it lies before left, then leaev left as it is, just update dic[s[right]]=right 
        while(right<len(s)):
            if s[right] in dic:
                # this statement means that either left have crosssed s[right], then fine, else make it cross s[right] 
                left=max(dic[s[right]]+1,left)
            # save the ans
            mx=max(right-left+1,mx)
            dic[s[right]]=right
            right+=1    
        return mx            
S="abcabc"
print(longest_substring_with_all_unique_char(S))
print(longest_substring_with_no_repeat_hash_approach(S))