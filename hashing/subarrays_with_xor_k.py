#refer Strivers placement series

# task- Given- array, k, find number of possible subarrays with XOR k
# approach best-  Observation- XOR sum of any array element can be broken into two parts k^Y(XOR of remainig array) = XOR of array
#                   k^ Y = XOR so Y= XOR^k here XOR is prefix XOR till this point, k is given
#                   so we have to find all such Y's(subarrays whose prefix xor is Y), and update count

def subarrays_with_xor_k(arr,k):
    #will use hash map to store values of Y(prefix Xor till current point) and its count as key

    dic={}

    prefix_xor=0
    count=0
    for a in arr:
        prefix_xor^=a

        # current prefix_xor is k, so thiss also be a ans, so increase count
        if prefix_xor==k:
            count+=1

        #  prefix_xor^k is that Y which we are seraching , if such Y present , add its count to main count variable
        if prefix_xor^k in dic:
            count+=dic[prefix_xor^k]

        if prefix_xor in dic:
            dic[prefix_xor]+=1
        else:
            dic[prefix_xor]=1  

    return count
arr=[4,2,2,6,4]
k=6
print(subarrays_with_xor_k(arr,k))
