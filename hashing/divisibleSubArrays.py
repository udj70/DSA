#find number of sum arrays with given sum k
def divisibleSubarr(arr,k):
    c_sum=[0] #cummulative sum array to store sum of all elemnt till  that index
    s=0
    #hashing all possible modulus values
    count=[0]*(k+1) #freq of remainder values which belongs in range [0,k-1]
    for a in arr:
        
        s+=a
        c_sum.append(s)
        count[s%k]+=1
        
        
        #choose b and a in c_sum such that (b-a)%k==0 i.e. b%k==a%k
        #group count of all such array element with same % value in freq aaray
    num_subarr=0
    for c in count:
        if c>1:
            num_subarr+=c*(c-1)//2  #nC2 i.e. no of ways of selecting any to elemnt with same modulas
    # add the elements which 
    # are divisible by k itself  
    # i.e., the elements whose c_sum%k= = 0 
    num_subarr+=count[0]    
    return num_subarr
arr=[1,1,1,1,1]
print(divisibleSubarr(arr,2))         
'''
def subCount(arr, n, k): 
  
    # create auxiliary hash 
    # array to count frequency 
    # of remainders 
    mod =[] 
    for i in range(k + 1): 
        mod.append(0) 
    
    # Traverse original array 
    # and compute cumulative 
    # sum take remainder of this 
    # current cumulative 
    # sum and increase count by 
    # 1 for this remainder 
    # in mod[] array 
    cumSum = 0
    for i in range(n): 
        cumSum = cumSum + arr[i] 
        print(cumSum)
        # as the sum can be negative, 
        # taking modulo twice 
        mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1
      
    
    result = 0  # Initialize result 
    print(mod)
    # Traverse mod[] 
    for i in range(k): 
    
        # If there are more than 
        # one prefix subarrays 
        # with a particular mod value. 
        if (mod[i] > 1): 
            result = result + (mod[i]*(mod[i]-1))//2
       
    # add the elements which 
    # are divisible by k itself  
    # i.e., the elements whose sum = 0 
    result = result + mod[0] 
       
    return result''' 
arr=[1,1,1,1,1]
print(divisibleSubarr(arr,2))






