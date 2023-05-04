#task- Given Two Strings, check if they are scrambled.
# problem statement link- https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmU5MTREN3dlbG9YZWtqYk9TTTFzSTMwS1NWUXxBQ3Jtc0tuNFpoek44WUFYSW1IUUJwVnNvaDZVaUhvdUtZNGNsV2lDaVZpdG94azAtVHlMSEJzQWRIa0hyQ0FyZ1drYktMY3NieUlobEI5cXg3WE9ZQmRFTW9HR1FIdW9nZFk2Tlk2UExQekxpM2pMSkNaanM0NA&q=https%3A%2F%2Fwww.interviewbit.com%2Fproblems%2Fscramble-string%2F&v=SqA0o-DGmEw

# approach- MAM based approach, check for all possible partition, break S1 at any random position,
# check for two condition
# 1. solve (first part of s1 ,first part of s2) and solve(last part of s1 ,last part of s2) i.e. if both  become means no swapping required
# 2. solve (first part of s1, last part of s2 of same length) and solve( last part of s1, last part of s2 of same length)

# if any of the condition satisfy i.e strings are scrambled
#return True
# TC- Exponential O(2^k +2^(n-k)), because making 4 recursive calls at each partition

# Memoize data, create dic, save some conbination of s1 and s2 as key and its answer as value, to avoid overlapping calls
# TC-(N^3) {recheck}
global dic

    
def solve(s1,s2):
        global dic
        # if strings are same, then they are scrambled
        if s1==s2:
            return True
        
        # if string have one character and not same, so not scrambled
        if len(s1)<=1:
            return False
        flag=False
        # create unique
        key=s1+" "+s2

        # check if this key already present
        if key in dic:
            return dic[key]
        n=len(s1)
        for i in range(1,len(s1)):
            # check both the condition for each i, if found true then break
            if ((solve(s1[0:i],s2[0:i]) and solve(s1[i:], s2[i:])) or (solve(s1[0:i], s2[n-i:]) and solve(s1[i:], s2[0:n-i]))):
                flag=True
                break
        dic[key]=flag
        return flag
def isScramble( s1: str, s2: str) -> bool:
        global dic
        dic={}
        # if two strings are of diffeent length, then they are not scrambled
        if len(s1)!=len(s2):
            return False
        # can add one more optimization, that is if both strings are not anagrams of each others , then they cant be scrambled
        return solve(s1,s2)
s1="rgeat"
s2="great"
print(isScramble(s1,s2))