# Definition for a binary tree node.
# find vertical order traversal of tree
# approach - perform LOT keep track of h_value, level_value, create map of h_value, 
#            and store tree node corresponding to each h_value
#            note- if two or more value are present at same h_value and l_value i.e overlapping nodes, so sort them then store in h_map
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root):
        h_map={}
        queue=[[root,0,0]]
        mn=float('inf')
        mx=float('-inf')
        
        while(len(queue)):
            element=queue.pop(0)
            node=element[0]
            h_value=element[1]
            l_value=element[2]
            mx=max(mx,h_value)
            mn=min(mn,h_value)
            if h_value in h_map:
                temp=[[node.val,l_value]]
                # if this h_value and l_value present in map already, sort them, then store again
                while(len(h_map[h_value]) and h_map[h_value][-1][1]==l_value):
                    p=h_map[h_value].pop()
                    temp.append(p)
                temp.sort(reverse=True)
                while(len(temp)):
                    p=temp.pop()
                    h_map[h_value].append(p)
                    
            else:
                h_map[h_value]=[[node.val,l_value]]
            if node.left:
                queue.append([node.left, h_value-1,l_value+1])
            if node.right:
                queue.append([node.right,h_value+1,l_value+1])
            
        ans=[]
        for i in range(mn,mx+1):
            ans.append([h[0] for h in h_map[i]])
        return ans
root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(6)
root.right=TreeNode(3)
root.right.left=TreeNode(5)
root.right.right=TreeNode(7)

s=Solution()
print(s.verticalTraversal(root))