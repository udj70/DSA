#task- subtract 1 from number represent by LL
#approach 1- save number in temp, subtract 1, then put numbers back in LL, TC-O(2*N)
#approach 2- make recursive calls utill head is none, then return -1 as borrow, subtract bowrrow from current element, return updated borrow if there
#           TC-O(N)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def subtractOne(head):
    if head is None:
        return -1
    borrow=subtractOne(head.next)
    if borrow==-1:
        #if zero, i.e we have to borrow from previous digit, so new borrow is -1
        if head.data==0:
            head.data=9
            return -1
        else:
            head.data-=1
    return 0
def print_LL(head):
    while(head):
        print(head.data,end="")
        head=head.next
head=Node(1)
head.next=Node(0)
head.next.next=Node(0)
#print_LL(head)
subtractOne(head)
print_LL(head)