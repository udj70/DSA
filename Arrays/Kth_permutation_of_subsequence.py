# task- Given -n create array elements 1->n, now find , kth number permutation
# approach 1- generate all permutations by recursion, save it in answer array, then sort the ans array, fetch kth permution
#               TC- O(n!*n)+O(n!LogN) for sorting, SC-O(n!)
# approach 2- divide n! permutions in blocks of size (n-1)!, n!//n =n-1 ! , (k-1)th subsequence first element will 
#               lie in k//(n-1)! block, 
# refere strivers code




def getPermutation(n,k):
    fact=1
    numbers=[]
    for i in range(1,n):
        fact=fact*i
        numbers.append(i)
    #fact contains intial block size i.e (n-1)!
    numbers.append(n)
    ans=""

    # considering 0 based indexing, we will serach for k-1 subsequence number
    k=k-1
    while(True):
        # k//fact is block number
        ans+=str(numbers[k//fact])
        #remove that  number from numbers, as it is included in permutation
        numbers.remove(numbers[k//fact])
        # if numbers i empty i.e permutation is made
        if len(numbers)==0:
            break
        # remainig permutions yet to be tracked is k% fact
        k=k%fact

        # new blcok size will be (len(numbers)-1)!
        fact=fact//len(numbers)
    return ans
n=4
k=12
print(getPermutation(n,k))