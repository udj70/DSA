#task- given an array find, quadruples such that there sum is S
#approach 1- first sort the array, then use use there loops to pick 3 element, and fourth element can be picked by binaryserach in remaining array
#           TC- O(n3logN) + O(n2)

#approach 2- sort, use two loops two get first two elements, then remaining 2 elemetn sum will be S-(i+j), so remaining atwo elemtn can be found by 2 sum approach
#           TC-O(n3) +O(n2)

def quadrapules(arr, S):
    quads=[]
    arr.sort()
    for i in range(len(arr)-3):
        for j in range(i+1,len(arr)-2):

            # till here we got two elments
            # remainig sum= targetsum- (arr[i]+arr[j])
            remaining_sum= S- (arr[i]+arr[j])

            # find this remaining sum in right part
            front=j+1
            last=len(arr)-1
            while(front<last):
                if arr[front]+arr[last]==remaining_sum:
                    quads.append([arr[i],arr[j],arr[front],arr[last]])
                    break
                elif arr[front]+arr[last]<remaining_sum:
                    front+=1
                else:
                    last-=1
    return quads

arr=[1,3,2,3,1,3,3,3,2,2,4,4,4,4,5,5]
S=7
print(quadrapules(arr,S))






