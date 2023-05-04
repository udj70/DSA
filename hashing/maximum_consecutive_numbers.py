#task - Given- unsorted array, find max length consecutive element subsequence

# approach 1- sort aaray, use sliding window TC- O(NlogN)
# approach 2- create hash map, traverse it, first find smallest element, then search for all consecutive element starting with it

def maximum_length_consecutive_subsequence(arr):
    dic={}
    for a in arr:
        dic[a]=False
    ans=0
    for a in arr:
        if a-1 in dic:
            continue
        else:
            start=a
            if not dic[start]: 
                temp=1
                dic[start]=True
                while(True):
                   
                    if start+1 in dic:
                        temp+=1
                        dic[start+1]=True
                        start=start+1
                    else:
                        break
                ans=max(temp,ans)
    return ans

arr=[102,4,101,100,3,1,2]
print(maximum_length_consecutive_subsequence(arr))
                        
