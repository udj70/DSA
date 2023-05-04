#task- Given- rowwise sorted and columnwise sorted matrix, find an element
#approach 1- start from first row last element, increase j if ele is greater then current, else i+1
            # TC O(m+n)
#approach2 - find floor of element in first row return col, then find element in that row
            #tc- O(logN+logM)

#search floor in first row
def find_floor_in_row(mat,ele):
    ans=-1
    start=0
    end=len(mat[0])-1

    while(start<=end):
        mid=start+(end-start)//2
        if mat[0][mid]==ele:
            ans=mid
            break
        if mat[0][mid]<ele:
            ans=mid
            start=mid+1
        else:
            end=mid-1

    return ans
#binary search in col
def find_element_in_column(mat,ele,col):
    ans=-1
    start=0
    end=len(mat)-1

    while(start<=end):
        mid=start+(end-start)//2
        if mat[mid][col]==ele:
            ans=mid
            break
        if mat[mid][col]<ele:
            start=mid+1
        else:
            end=mid-1

    return ans
def search_in_matrix(mat,ele):
    j=find_floor_in_row(mat,ele)
    i=find_element_in_column(mat,ele,j)
   
    return [i,j]
mat=[[10,20,30,40],
      [15,25,35,45],
      [16,26,36,46]
    ]
print(search_in_matrix(mat,35)) #(1,2)
