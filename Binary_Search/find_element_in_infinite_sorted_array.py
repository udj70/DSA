#task- Given- infinte sorted array, find element
#approach- we dont know end here, so we will assume end at 0+1 index, then gradually increase it to get proper range.
from binary_search import bin_search
def find_element_in_infinie_sorted_array(arr,element):
    start=0
    end=1 # assumed

    while(arr[end]<element):
        start=end
        end=end*2
    ans=bin_search(arr,start,end,element)
    return ans
#just an algo, not running code
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15..........]
element=14 
find_element_in_infinie_sorted_array(arr,element)


    
    