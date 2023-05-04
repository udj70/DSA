# task - Given a sorted array of interger with duplicates values
# return count of unique vvlues

#refer strivers video

# approach 1- use  set , return len of set
# tc- O(N) sc- O(N)

# approach 2- use two pointers , i and j, increment i only when different vlue is found at j , swap with i+1
# Return len(arr[0:i+1])
# tc= O(N)
# sc= O(1)

def remove_duplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return len(arr[:i+1])
arr=[1,1,1,2,2,2,3,3,5,5,5]
print(remove_duplicates(arr))
