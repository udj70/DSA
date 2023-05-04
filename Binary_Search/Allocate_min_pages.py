# task- Given- given books pages in array, assign books to k students in such a way diffrence of pages read ny each student is least, and books chosen are in asc order
# approach- minimum pages read will be max amongs pages, and maximum pages read will sum of all pages
# apply BS and find count of pages between min max which is most appropiate to distribute among K students

#refer aditya verma
# refer striver

# tc- O(nlogn)

def isValid(pages,k,size):
    #code to if k partitions are possible with max sum==size
    students=1
    sum_=0
    i=0
    while(i<len(pages)):
        sum_+=pages[i]
        if sum_>size:
            # if sum is more then size then intialise sum with current page for further calculation, 
            # and increase count of students
            sum_=pages[i]
            students+=1
        if students>k:
            return False
        i+=1
    return True
def Alllocate_min_pages(pages,k):
    # atleast one book we have to assign, so will start from max size book
    start=max(pages)
    #will end upto all books to one student(worst case)
    end=sum(pages)
    ans=-1
    while(start<=end):
        mid=start+(end-start)//2
        #if k partitions is possible in pages array with max size mid i.e current page can be ans, and check in left part
        if isValid(pages,k,mid):
            ans=mid
            end=mid-1
        else:
            #if current size mid is possible  to be distributed then increase size, go in right of mid
            start=mid+1
    return ans  

pages=[10,20,30,40]
k=3
print(Alllocate_min_pages(pages,k))