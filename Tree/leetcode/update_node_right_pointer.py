"""
# Definition for a Node.
"""

# task- given perfect BT, connect all nodes next pointer to its next right in its level
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return None

        # try to dry run and imagine
        if root.left and root.right:
            root.left.next=root.right
            if root.next:
                root.right.next=root.next.left
            
            self.connect(root.left)
            self.connect(root.right)
        return root    
    
    #traverse using right pointer
    def traverse(self,root):
        print(root.val,end="")
        start=root.left
        nextStart=start.left
        while(True):
            while start:
                print(start.val,end="")
                start=start.next
            if not nextStart:
                break
            start=nextStart
            if nextStart.left:
                nextStart=nextStart.left
            else:
                nextStart=None
        
s=Solution()
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
new_root=s.connect(root)
s.traverse(new_root)
