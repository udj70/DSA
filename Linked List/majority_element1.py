# task- given linked list of integer, find majority element such that its frequency is more then N//2, here is len of LL
# approach 1- create array, sort it, then calculate max element by sliding window
#            tc- O(nlogn) + O(n), sc- O(n)
# approach 2- traverse LL and store element and its frequency in hash map,
#             now traverse hash map and get majority element
#            tc- O(n) sc- O(n)
# approach 3- moore's voting algo
#             traverse linked list, track majority element count it, when any minority element come reduce count of current majority element
#             at the end we will have one majority element, because as majority eleemnt is more then n//2, so at end minority element will not be able to cut the frequency of majority eleemnt to 0
def majority_element1(head):
    temp=head
    majority_element=-1
    count=0
    while(temp):
        val=temp.data
        if count==0:
            majority_element=val
            count+=1
        elif val==majority_element:
            count+=1
        else:
            count-=1
        temp=temp.next
    return majority_element