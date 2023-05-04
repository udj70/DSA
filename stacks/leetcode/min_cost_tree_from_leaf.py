'''
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.


Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.


refer leetcode for diagrams
'''

# approach- Observation- only adjancent node can be picked, not any pair(if any pair is allowed then it can be same as huffman encoding)
#                      - here when two leafs are picked then their multiplication answer is added to answer and larger leaf value is kept, smaller one is deleted(
#                         reason- we have to keep track of largest leaf in subtree while calculating parent as per question requirement)
#            solution- as we know we have to delete smaller leaf evry time, so while deleting a leaf 'a' we multiply it with min(just,left,just_right), save ans, and delete
#                      so by using monotonic stack, we calculate NGR, so if current element is larger then stack top. we pop it, so that popped element is smaller then current elemet and stack top
#                       now before removing popped element, we multiply it with smaller(current element, stack.top) , and then remove it  
class Solution:
    def mctFromLeafValues(self, arr):
        stack=[float('inf')]
        ans=0
        for a in arr:
            while(stack[-1]<=a):
                removed_smaller=stack.pop()
                # before deleting this leaf node, calculte product with smaller in left or right, and then delete
                ans+=removed_smaller*min(stack[-1],a)
            stack.append(a)
        while(len(stack)>2):
            #remaing element will be poped as they are already in decending order in stack, leave last last element pop remainig
            ans+=stack.pop()*stack[-1]
        return ans