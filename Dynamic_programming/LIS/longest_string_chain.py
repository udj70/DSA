# task- Given a strings array, find longest string chain such that prev string in chain differ by only one char with curr string
# same as LIS

def compare(s1,s2):
    if len(s1) != len(s2)+1: return False

    first=0
    second=0

    # here s1 will always be larger size, for that we sort the string array
    while(first<len(s1)):
        if second<len(s2) and s1[first] == s2[second]:
            first+=1
            second+=1
        else:
            # if does not match. i.e some different char in first, move first
            first+=1
    if first==len(s1) and second==len(s2): # if both reahces end at same time
        return True
    return False

def LSC_dp_alternate_print(arr):
    dp=[1]*len(arr) # intially LIS is 1
    arr.sort(key=lambda s:len(s))
    # to store index of prev of current cell, for backtracking purpose
    idx_hash=[i for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if compare(arr[i],arr[j]):
                if dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    idx_hash[i]=j
                # dp[i] = max(dp[i],dp[j]+1)
    
    idx=dp.index(max(dp))
    #print(idx_hash)
    # start backtracking from index
    count=0
    while(count<max(dp) and idx>=0):
        print(arr[idx],end=" ")
        idx=idx_hash[idx]
        count+=1
    return 
arr=['a','abc','ab','ac','aca']

LSC_dp_alternate_print(arr)

