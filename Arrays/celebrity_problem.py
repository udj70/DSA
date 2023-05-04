#task - Given- given n persons and matrix telling whether x person know y, find celebrity among them, i.e a person who is known by everyone, but doesnt knows anyone else
# approach 1- create two array indegree, outdegree, traverse matrix, and fill outdegree[i] if i know j, and indegree[i] if j knows i  
#           , if there is any element with indgree n-1 and out degrees 0, i.e celebrity
#           TC- O(NxN) Sc- O(N)


# approach 2- use stack, pop two elements from top, if a knows b, then a cannaot be celebrity, so push back b, else pushback a
#           last element remaining will be potential clebrity, recheck once by travesing all peoples
#           TC- O(N) SC- O(N)

# approach 3- make recursive call on n-1 peoples, and find potential candidate, 
#               if potential candidate know n-1th person, n-1th person can be celebrity, return n-1
#               if  potential candidate does not know n-1th person, potential candidate is celeb, return it
#               if no potential candidate, return -1
#               TC- O(N) SC-O(1)

#approach 4- use two pointers, i=0, j=len(arr)-1, if i knows j then i can't be celeb, i++
#                                                 else j++
#               TC- O(N) SC- O(1)

from sympy import false


def find_celeb(knows):
    i=0
    j=len(knows[0])-1
    while(i<j):
        if knows[i][j]:
            i+=1
        else:
            j-=1
    celeb=i

    #recheck
    flag=False
    for j in range(len(knows[0])):
        if j!=celeb:
            if knows[j][celeb] and not knows[celeb][j]:
                continue
            else:
                flag=True
                break
    if not flag:
        return celeb
    return -1



knows = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]
print(find_celeb(knows))