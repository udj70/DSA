# task - given two sorted LL, l1 and l2, merge them to form new LL
# approach 1- create new LL by merging l1 and l2, tc-O(n+m) sc-O(n+m)
# approach 2- inplace merging
#             intuition-
#             l1 will always point to smaller element, now move l1 till it is smaller then l2, keep track of previous,
#             as l1 become more then l2, point previous.next to l2, and swap l1 and l2 as l2 will be new smaller for next traversal
#             perform above steps untill one of them become empty LL

def merge_LL(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    # make l1 always point to smaller node
    if l1.data>l2.data:
        l1,l2=l2,l1
    res=l1
    while(l1 and l2):
        prev=None
        while(l1 and l1.data<=l2.data):
            prev=l1
            l1=l1.next
        prev.next=l2

        l1,l2=l2,l1
    return res

        
    