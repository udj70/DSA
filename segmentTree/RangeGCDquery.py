import math
def findGCD(st,ss,se,qs,qe,si):
    #ss->current range start
    #se->current range end
    #qs->query range start
    #qe->query range end
    #si->current st node index

    #if query start is greater then current range end OR if query end is less then current range start,
    #then query range is not available in current range return 0
    if ss>qe or qs>se:
        return 0
    #if query is completly is in current range, then return current range gcd value    
    if qs<=ss and qe>=se:
        return st[si]
    #else calculate mid    
    mid=ss+(se-ss)//2 
    #and check query range in smaller ranges
    return math.gcd(findGCD(st,ss,mid,qs,qe,2*si+1),findGCD(st,mid+1,se,qs,qe,2*si+2))   
            

def gcdOfRange(st,start,end,n):
    #if desired query range is out of range of array then the query parameters are invalid
    if start<0 or end>n-1 or start>end:
        print("invalid arguments")
        return
    return findGCD(st,0,n-1,start,end,0)

def createST(arr,ss,se,si,st):
    #base case if number of element in range is one
    if ss==se:
        st[si]=arr[ss]
        return st[si]
    #else calculate mid    
    mid=ss+(se-ss)//2 
    #and call recursively for ss to mid and mid+1 to se, both will return gcd of 1st and 2nd half 
    st[si]= math.gcd(createST(arr,ss,mid,2*si+1,st),createST(arr,mid+1,se,2*si+2,st))
    #and gcd of complete array will gcd of both returned value
    #then return gcd of current range
    return st[si]

def sizeOfSt(arr,n):
    #height of tree can be calculated from number of leaf nodes of complete tree using below formula
    height=math.ceil(math.log2(n))
    #number of nodes in st will be calculated from height using below formula
    size=2*pow(2,height)-1
    st=[0]*size
    #fill the st Array from array element
    createST(arr,0,n-1,0,st)
    return st
arr=[2, 3, 6, 9, 5]
#In segment tree all the aaray elemnt are leaf nodes of tree
#sizeofst() will calculate size of segment tree array by the lenght of of array
st=sizeOfSt(arr,len(arr))
print(gcdOfRange(st,1,3,len(arr)))




