# task- given few sorted linked lists attached with each other by next pointer at root
#       each linked list node are connected by bottom pointer
#       head -> 1 -> 4 -> 5 - > Null
#              |    |    |
#              2    6    7
#              |    |
#              5    7    

# approach - same as merging two LL, just here we have multiple LL, use recursion to one by one merging them
# refer striver
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next=None
        self.bottom=None

def merge_LL_util(a,b): # a and b are LL
    temp = Node(0)
    res = temp
    while(a and b):
        if a.data<b.data:
            temp.bottom=a
            a=a.bottom
            temp=temp.bottom
        else:
            temp.bottom=b
            b=b.bottom
            temp=temp.bottom
    if a:
        temp.bottom = a
    elif b:
        temp.bottom = b
    return res.bottom


def merge_LL(head):

    # if head is null i.e empty LL, return None else if only one LL is there so simply return its head
    if not head or not head.next:
        return head
    # head new next will be all then remaining merged LL head
    head.next = merge_LL(head.next)

    # now merge current head and head.next
    new_head = merge_LL(head,head.next)
    return new_head

