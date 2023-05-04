#task- Given- A string S1, String s2, find smallest substring in S1 which have all the characters of s2 in it.
#approach- Use hash map to store charcters of s2 and their count. Reduce the count when chracters occurs.
#refer - aditya verma
def min_window_substring(s1, s2):
    dic={}
    for ch in s2:
        if ch in dic:
            dic[ch]+=1
        else:
            dic[ch]=1
    count=len(dic)
    mn=float('inf')
    i=0
    j=0

    while(i<=j):
        # if count is zero , i.e. current window have covered all chars of s2, calculate ans
        if count==0:
            #ans
            mn=min(mn,j-i)
            #after calculation reduce window size from left
            if s1[i] in dic:
                #if i contains required char the  increase count
                if dic[s1[i]]==0:
                    count+=1
                dic[s1[i]]+=1
            i+=1
        elif j<len(s1):
            #if j is not at last+1
            if s1[j] in dic:
                # decrement if j have required char
                dic[s1[j]]-=1
                # if after decrement current char count became zero. i.e we got all count of that char, hence reduce count
                if dic[s1[j]]==0:
                    count-=1
            j+=1
        else:
            break
    return mn
                
        
s1="otaxvtoat"
s2="toat"
print(min_window_substring(s1,s2))