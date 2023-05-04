# task- Give a string, count number of distinct substring
# approach1 - create hash set of string of string formed by linearly traversing in two loops
#             tc- O(n^2) sc-O(n^3) refere striver for explanation
# approach 2- use trie, TC is same, but better is Space complexity, in worstcase 26*26*26....n

class Node:
    def __init__(self):
        self.children=[None]*26
class Trie:
    def __init__(self):
        self.root=Node()
    def count_subtring(self,word):
        cnt=0
        for i in range(len(word)):
            root=self.root
            for j in range(i,len(word)):
                if root.children[ord(word[j])-ord('a')] is None:
                    cnt+=1
                    root.children[ord(word[j])-ord('a')]=Node()
                    root=root.children[ord(word[j])-ord('a')]
        return cnt+1
s='abab'
t=Trie()
print(t.count_subtring(s))