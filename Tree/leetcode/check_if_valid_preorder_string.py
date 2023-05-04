#task- refer leet code problem st.
#approach, at every node check if left and right both return valid answers
global index
class Solution:
    def solve(self,preorder):
        global index
        #base conditions, dry run and analyze
        if index>len(preorder)-1:
            return False
        if index==len(preorder)-1:
            if preorder[index]=="#":
                return True
            else:
                return False
        if preorder[index]=="#":
            return True
        
        left=False
        right=False
        index+=1
        left=self.solve(preorder)
       
        index+=1
        right=self.solve(preorder)
        
        
        return left and right
    def isValidSerialization(self, preorder: str) -> bool:
        global index
        index=0
        preorder=preorder.split(",")
        #print(preorder)
        temp=self.solve(preorder)
        if index<len(preorder)-1:
            return False
        else:
            return temp
s=Solution()
preorder="9,#,#,1"
print(s.isValidSerialization(preorder))