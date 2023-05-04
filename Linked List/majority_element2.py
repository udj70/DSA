# task- given linked list of integer, find majority element such that its frequency is more then N//3, here N is len of LL
# approach 1- create array, sort it, then calculate max element by sliding window
#            tc- O(nlogn) + O(n), sc- O(n)
# approach 2- traverse LL and store element and its frequency in hash map,
#             now traverse hash map and get majority element
#            tc- O(n) sc- O(n)
# approach 3- boyce moore's voting algo
#             here only differnce is there can be two majority element, so have two variables 
#             traverse linked list, track majority element count it, when any minority element come reduce count of both majority element
#             at the end we will have one or two majority element, because as majority eleemnt is more then n//3, so at end minority element will not be able to cut the frequency of majority eleemnts to 0
def majority_element2(head):
    temp=head
    majority_element1=-1
    majority_element2=-1
    count1=0
    count2=0
    while(temp):
        val=temp.data
        if count1==0:
            majority_element1=val
            count1+=1

        elif count2==0:
            majority_element2=val
            count2+=1
        
        elif val==majority_element1:
            count1+=1
        elif val==majority_element2:
            count2+=1
        else:
            count1-=1
            count2-=1
        temp=temp.next
    # count again and cross check

    temp=head
    count1=0
    count2=0
    N=0
    while(temp):
        if temp.data==majority_element1:
            count1+=1
        if temp.data==majority_element2:
            count2+=1
        temp=temp.next
        N+=1
    res=[]
    if count1>N//3:
        res.append(majority_element1)
    if count2>N//3:
        res.append(majority_element2)
    return res