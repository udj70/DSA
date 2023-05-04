#Split the given string into Primes : Digit DP
#constraint-prime number in the range of 1 to pow(10,6)
import math


def IsPrime(number):
    number=int(number)
    flag=0
    for i in range(2,math.ceil(math.sqrt(number))):
        if number%i==0:
            flag=1
            break
    if flag==0:
        return True
    return False
def SplitIntoPrime(number):
    splitDp=[-1 for i in range(len(number))]
    numlen=len(number)
    for i in range(1,numlen+1):
        #from 0 to i-1, if number is prime, update dp[i-1]=1
        if IsPrime(number[0:i]):
            splitDp[i-1]=1
        j=1 
        #now start from i till j, max diff between i and j is 6
        while(j<=6 and i+j<numlen+1):
            if IsPrime(number[i:i+j]):
                # if number from i-> i+j-1 is prime
                # then dp[i+j-1] update with dp[i-1]+1
                if splitDp[i+j-1]==-1:
                    splitDp[i+j-1]=splitDp[i-1]+1
                else:
                    splitDp[i+j-1]=min(splitDp[i+j-1],splitDp[i-1]+1)
            j+=1             
    return splitDp[numlen-1]
print(SplitIntoPrime('1349935'))  
print(SplitIntoPrime('133'))   





    