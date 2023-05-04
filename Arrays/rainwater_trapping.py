
# tc-O(n) sc-O(2n)
def rainwater_trapped(arr):
    left=[]
    right=[]
    ma=0
    for a in arr:
        ma=max(ma,a)
        left.append(ma)
    ma=0    
    for a in arr[::-1]:
        ma=max(ma,a)
        right.append(ma)
    right.reverse()    
    water=[]
    for i in range(len(arr)):
       water.append(min(left[i],right[i])-arr[i])
    return sum(water)           

buildings=[1,3,0,0,2,0,4,3,4,2]
print(rainwater_trapped(buildings))

# better approach- two pointer, tc-O(n), sc-O(1)
# intuition- refer strivers video
def rainwater_trapped_opt(buildings):
    l=0
    r=len(buildings)-1
    left_max=0
    right_max=0
    res=0
    while(l<=r):
        if buildings[l]<=buildings[r]:
            if buildings[l]>=left_max:
                left_max=buildings[l]
            else:
                res+=left_max-buildings[l]
            l+=1
        else:
            if buildings[r]>=right_max:
                right_max=buildings[r]
            else:
                res+=right_max-buildings[r]
            r-=1
    return res
buildings=[1,3,0,0,2,0,4,3,4,2]
print(rainwater_trapped_opt(buildings))

