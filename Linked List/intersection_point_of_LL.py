# task- given two linkedlist such that they may intersect at certain node, find intersection point if present
# approach 1- pick one node, and check in other LL, if that node present return, tc- O(n^2)
# approach 2- store one LL values in hash, and traverse other ll and check first matching node, tc-O(n), sc-O(n)
# approach 3- in fist traversal find difference in length of two LL, shift head pointer of larger list by differnce value, 
#             and then again traverse both LL simultaneously, will meet and insection point at same point, tc-O(m)+O(m-n)+O(n)
# approach 4- move head pointer of both LL, when one of it reaches end, pick it and place that point to other LL start, 
#             then again move both of them, when second one reaches end , pick it and place it in another LL head, now 
#             now we can obvserve that both came at prallele starting points

def intersection_point(head1, head2):
    if not head1:
        return None
    if not head2:
        return None
    a=head1
    b=head2
    while(a!=b):
        a=head2 if a==None else a.next
        b=head1 if b==None else b.next
    return a