# task- Clone linked list- It have next and random pointer



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.random=None

# approach 1- Hash map based approach- traverse each node in LL and make one dummy node with same value and save in hash map
#             traverse LL again, fill those pointer values of dummy nodes same as current node

def clone_LL(head):
    dic={}
    temp=head
    while(temp):
        dummy=Node(temp.data)
        dic[temp]=dummy
        temp=temp.next
    temp=head
    while(temp):
        dic[temp].next=dic[temp.next]
        dic[temp].random=dic[temp.random]
        temp=temp.next
    new_head=dic[head]
    return new_head

# approach 2- Insert dummy nodes in between

#   4-> 4' -> 5-> 5'-> 6 -> 6'->7 ->7' ->8 ->8'
# now re- traverse for each alternate 

def clone_LL_insert(head):

        temp=head
        while(temp):
            dummy=Node(temp.data)
            dummy.next=temp.next
            temp.next=dummy
            temp=dummy.next
        
        # random pointer correction
        temp=head
        while(temp):
            if temp.random:
                temp.next.random=temp.random.next
            temp=temp.next.next
        new_head=head.next
        temp=head
        while(temp):
            old_next=temp.next.next
            if old_next:
                temp.next.next=temp.next.next.next
            temp.next=old_next
            temp=temp.next
        return new_head


node1=Node(4)
node2=Node(5)
node3=Node(6)
node4=Node(7)
node5=Node(8)


head=node1

head.next=node5
head.random=node4

head.next.next=node3
head.next.random=node1

head.next.next.next=node4
head.next.next.random=node1

head.next.next.next.next=node2
head.next.next.next.random=node2

new_head=clone_LL_insert(head)
while(new_head):
    print(new_head.data)
    new_head=new_head.next