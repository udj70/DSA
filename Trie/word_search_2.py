'''
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''
class Node:
    def __init__(self):
        self.children=[None]*26
        self.end=False
class Trie:
    def __init__(self):
        self.root=Node()
    def addWord(self, word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is None:
                root.children[ord(ch)-ord('a')]=Node()
            root=root.children[ord(ch)-ord('a')]
        root.end=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t=Trie()
        for word in words:
            t.addWord(word)
        row,col=len(board),len(board[0])
        ans,visit=set(),set()
        
        def dfs(r,c,word,node):
            if r==row or c==col or r<0 or c<0 or ((r,c) in visit) or (node.children[ord(board[r][c])-ord('a')] is  None):
                return
            visit.add((r,c))
            node=node.children[ord(board[r][c])-ord('a')]
            word+=board[r][c]
            if node.end:
                ans.add(word)
                node.end=False
            dfs(r+1,c,word,node) 
            dfs(r-1,c,word,node) 
            dfs(r,c+1,word,node) 
            dfs(r,c-1,word,node) 
            visit.remove((r,c))
        for r in range(row):
            for c in range(col):
                dfs(r,c,"",t.root)
        return list(ans)