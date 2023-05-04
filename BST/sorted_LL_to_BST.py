# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val,end="")
        self.inorder(root.right)

    def createTree(self,head):
        # if no no node, return None
        if not head:
            return None
        # if single node, create Tree node and return
        elif not head.next:
            return TreeNode(head.val,None,None)
        # if two nodes, create Treenode with first node and second as its right
        elif not head.next.next:
            return TreeNode(head.val,None,TreeNode(head.next.val,None,None))
        # more than two nodes
        else:
            # get middle by slow and fast pointer
            prev=None
            slow=head
            fast=head
            while(fast.next and fast.next.next):
                prev=slow
                fast=fast.next.next
                slow=slow.next
            prev.next=None

            # seperate list from middle, make prev.next null 
            # two LL created one started with head, and other with slow.next


            tNode=TreeNode(slow.val,None,None)
            tNode.left=self.createTree(head)
            tNode.right=self.createTree(slow.next)
            return tNode
    def sortedListToBST(self, head):
        return self.createTree(head)
s=Solution()
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

root=s.sortedListToBST(head)
s.inorder(root)

