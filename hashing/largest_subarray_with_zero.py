# task- Given- find longest subarray with sum of element zero
# approach best- build hash map(prefix sum-> index) while trversing, 
#               check if current prefix sum have already occured somewhere back in arr
#               i.e. intermediate sums is zero, thats why prefix sum does not changed, calculate that intermediate array length using index difference


def largest_subarray_with_zero_sum(arr):
    dic={}
    pre_sum=0
    ans=0
    for i in range(len(arr)):
        pre_sum+=arr[i]
        if pre_sum==0: #if sum till this point is zero, max length is complete subarray till this point
            ans=max(ans,i+1)
        else:
            #else check in dic 
            if pre_sum in dic:
                ans=max(ans,i-dic[pre_sum])
            else:
                dic[pre_sum]=i
        return ans

arr=[1,-1,3,2,-2,-8,1,7,10,23]
#arr=[-1,1,-1,1]
print(largest_subarray_with_zero_sum(arr))
