# Trie is datastructure used to create prefix trees
# it have node with alphabets hash as data member and end flag to mark end of word

# refer strivers series for more detail

class Node:
    def __init__(self):
        self.children=[None]*26
        self.end=False
class Trie:
    def __init__(self,Node):
        self.root=Node

    # insert in Trie , traverse all char in word and if current char is not present in childrens, 
    # add it and its reference should point to empty node
    # at last when all char of word is traversed assign end flag of empty node to True, it will be used while searching in trie

    def insert(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is None:
                root.children[ord(ch)-ord('a')]=Node()
            root=root.children[ord(ch)-ord('a')]
        root.end=True

    # search char by char, if at the end node end flag is True, that is word is present 
    def search(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is None:
                return False
            else:
                root=root.children[ord(ch)-ord('a')]
        if root.end:
            return True
        else:
            return False
    
    # search char by char, if all char present in trie, return true, else break in between
    def starts_with(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is None:
                return False
            root= root.children[ord(ch)-ord('a')]
        return True
        
t=Trie(Node())
t.insert('apple')
t.insert('apps')
print(t.search('apple'))
print(t.starts_with('ap'))