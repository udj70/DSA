
#generate N bit binary number with number of 1's is grater than or equal to 0's in nay prefix
def generateAllPrefix(num,count,N,one,zero):
    global ans
    if count==N:
        ans.append(num)
        return
    if one+1>=zero:
        generateAllPrefix(num+"1",count+1,N,one+1,zero)
    if zero<one:
        generateAllPrefix(num+"0",count+1,N,one,zero+1)
    return 
ans=[]
generateAllPrefix("",0,5,0,0)
print(ans)    

#input=generate 5 bit number
#output=['11111', '11110', '11101', '11100', '11011', '11010', '11001', '10111', '10110', '10101']