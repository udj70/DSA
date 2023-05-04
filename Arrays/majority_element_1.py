# task- Given array, print majority eleemnt among, majority eleemnt is element which occured more than n//2 times
#                    Note- majority element always exist
# approach 1- store count of element in hash map, and then check element whose freq is more than n//2
# approach 2- moore's voting algo, in this we maintain two variables, majority ele and count
#             conditions- 1. if curr eleemnt is equal to majority element, increament count
#                         2. if count==0, assign new element as majority element, and increment ccount
#                         3. else if curr eleemnt is not majority then decrement count
# intuition- we know that  , majority element occurs more than n//2 times, so while traversing in array, majority element count will be cancelled out by minority element count, 
#            but because majority element is more then n//2 so, at the end some count of majority element will remain.


def majority_element(arr):
    major_el=-1
    count=0
    for a in arr:
        if count==0:
            major_el=a
            count+=1
        elif major_el==a:
            count+=1
        else:
            count-=1
    return major_el
arr=[1,2,3,1,1,1]
print(majority_element(arr))