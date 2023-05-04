#task- Given- String S1 and String S2, find count of anagrams of S2 in given string S1
#approach 1- generate all anagrams of S2 and check in S1 by sliding window TC-O(n!)
#approach 2- use hash map of characters in S2 and store count ,
# as a character occur, reduce count of that charcter, if count of all the charcter become zero i.e. increase count of anagrams 

def count_occurence_of_anagrams(s1, s2):
    hash_map={}
    count=0
    for ch in s2:
        if ch in hash_map:
            hash_map[ch]+=1
        else:
            hash_map[ch]=1
    count=len(hash_map) #count of unique characters
    i=0
    j=0

    #take j to window size(size of s2) 
    k=len(s2)
    ans=0
    while(j<len(s1) and j<k):
        if s1[j] in hash_map:
            #if hash_map[s1[j]]>=1:
                hash_map[s1[j]]-=1
                if hash_map[s1[j]]==0:
                    count-=1
        if count==0:
            ans+=1
        j+=1
    
    while(j<len(s1)):
        if s1[i] in hash_map:
            if hash_map[s1[i]]==0:
                count+=1
            hash_map[s1[i]]+=1

        if s1[j] in hash_map:
            #if hash_map[s1[j]]>=1:
                hash_map[s1[j]]-=1
                if hash_map[s1[j]]==0:
                    count-=1
        if count==0:
            ans+=1
            #print(i)
        j+=1
        i+=1
    return ans
            
            
    
s1="cbaebabacd"
s2="abc"
print(count_occurence_of_anagrams(s1,s2))

#working code